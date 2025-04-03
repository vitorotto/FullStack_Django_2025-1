from django.urls import path

from . import views

urlpatterns = [
    path("teste", views.index, name="index"),
    path("dizeroi", views.dizer_oi, name="dizeroi"),
    path("somarnumeros", views.somar_numeros, name="somarNumeros"),
]
