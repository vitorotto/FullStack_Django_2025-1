from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Endereco

# Create your views here.


def lista_clientes(request):
    # pegando todos os clientes do banco de dados
    lista_clientes = Cliente.objects.all()
    enderecos = Endereco.objects.all()
    # renderizando a lista de clientes na template
    dados = {
        'clientes': lista_clientes,
        'enderecos': enderecos
    }
    return render(request, 'lista_clientes.html', dados)


def index(request):
    return render(request, 'index.html')
