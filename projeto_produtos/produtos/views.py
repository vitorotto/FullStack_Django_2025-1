from django.shortcuts import render
from .models import Produto

# Create your views here.


def index(request):
    return render(request, 'produtos/index.html')


def produtos(request):
    # Vamos pegar todos os produtos do banco de dados
    lista_produtos = Produto.objects.all()
    dados_index = {
        'frase': 'Frase para testar lá no Frontend',
        'nome': 'Lucas',
        'idade': 25,
        'produtos': lista_produtos,  # Passando a lista de produtos para o dicionario
    }
    return render(request, 'produtos/produtos.html', dados_index)
