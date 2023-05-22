from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente
from django.views.decorators.csrf import csrf_exempt

def cliente_list(request):
    clientes = Cliente.objects.all()

    # Você pode retornar os dados em formato JSON para serem consumidos pelo PyQt5
    data = {
        'clientes': [
            {'nome': cliente.nome, 'contato': cliente.contato}
            for cliente in clientes
        ]
    }
    return JsonResponse(data)
@csrf_exempt
def cliente_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        contato = request.POST.get('contato')
        Cliente.objects.create(nome=nome, contato=contato)

        # Você pode retornar uma resposta de sucesso
        return JsonResponse({'success': True})

    # Caso contrário, retorne uma resposta de erro
    return JsonResponse({'success': False, 'message': 'Método inválido'})


def buscar_cliente_por_nome(request):
    nome = request.GET.get('nome', '')

    clientes = Cliente.objects.filter(nome__icontains=nome)

    data = {
        'clientes': [
            {'nome': cliente.nome, 'contato': cliente.contato}
            for cliente in clientes
        ]
    }

    return JsonResponse(data)



