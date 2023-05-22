import sys
from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QListWidget
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de Janela com Busca")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        self.search_label = QLabel("Digite o nome a ser buscado:")
        layout.addWidget(self.search_label)

        self.search_input = QLineEdit()
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.on_search_clicked)
        layout.addWidget(self.search_button)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.network_manager = QNetworkAccessManager(self)

    def on_search_clicked(self):
        nome = self.search_input.text()

        url = QUrl("http://localhost:8000/contatos/buscar_cliente_por_nome/")
        query = QUrlQuery()
        query.addQueryItem("nome", nome)
        url.setQuery(query)

        request = QNetworkRequest(url)

        reply = self.network_manager.get(request)
        reply.finished.connect(self.on_request_finished)

    def on_request_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            response_data = reply.readAll().data().decode()
            response_json = json.loads(response_data)

            self.result_list.clear()

            if 'clientes' in response_json:
                clientes = response_json['clientes']
                for cliente in clientes:
                    nome = cliente.get('nome', '')
                    contato = cliente.get('contato', '')
                    self.result_list.addItem(f"Nome: {nome}, Contato: {contato}")

        else:
            self.result_list.clear()
            self.result_list.addItem("Erro na busca")

        reply.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



