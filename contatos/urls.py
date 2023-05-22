from django.urls import path
from . import views

app_name = 'contatos'

urlpatterns = [
    path('cliente_list/', views.cliente_list, name='cliente_list'),
    path('cliente_create/', views.cliente_create, name='cliente_create'),
    path('buscar_cliente_por_nome/', views.buscar_cliente_por_nome, name='buscar_cliente_por_nome'),
]
