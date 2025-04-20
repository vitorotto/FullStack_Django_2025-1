from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def lista_clientes(request):
    return HttpResponse("Olá, Você está na index do app clientes.")
