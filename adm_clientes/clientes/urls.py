from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("clientes/<int:id_cliente>/",
         views.detalhes_cliente, name="detalhes_cliente"),
    path("", views.index, name="index")
]
