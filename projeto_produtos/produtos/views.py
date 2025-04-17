from django.shortcuts import render
from .models import Produto
from django.db.models.functions import Lower


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


def produtos_por_preco(request):
    # Vamos pegar todos os produtos do banco de dados
    lista_produtos = Produto.objects.all().order_by('preco')
    dados_index = {
        'produtos': lista_produtos,  # Passando a lista de produtos para o dicionario
    }
    return render(request, 'produtos/produtos.html', dados_index)


def produtos_por_parametro(request, parametro):
    # Vamos filtrar os produtos com base no parâmetro e valor fornecidos
    if parametro == 'nome':
        lista_produtos = Produto.objects.all().order_by(Lower('nome'))
    elif parametro == 'preco':
        lista_produtos = Produto.objects.all().order_by('preco')
    elif parametro == 'descricao':
        lista_produtos = Produto.objects.all().order_by(Lower('descricao'))
    else:
        lista_produtos = Produto.objects.all().order_by('id')

    dados_index = {
        'frase': 'Frase para testar lá no Frontend',
        'nome': 'Lucas',
        'idade': 25,
        'produtos': lista_produtos,  # Passando a lista de produtos para o dicionário
    }
    return render(request, 'produtos/produtos.html', dados_index)

def produto_detalhes(request, id_produto):
    produto_filtrado = Produto.objects.get(id=id_produto)
    dados_produto_detalhes = {
        'produto': produto_filtrado,  # Passando o produto para o dicionário
    }
    return render(request, 'produtos/produto_detalhes.html', dados_produto_detalhes)
