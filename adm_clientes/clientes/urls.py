from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_clientes, name="index_clientes")
]
