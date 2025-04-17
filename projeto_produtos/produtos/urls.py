from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/preco/', views.produtos_por_preco, name='produtos_por_preco'),
    path('produtos/parametro/<parametro>',
         views.produtos_por_parametro, name='produtos_por_parametro'),
    path('produtos/<id_produto>', views.produto_detalhes,
         name='url_produto_detalhes'),
]
