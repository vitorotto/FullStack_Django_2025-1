from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, Você está na index do app pesquisas.")

# Create your views here.


def dizer_oi(request):
    return HttpResponse("A página diz Olá")


def somar_numeros(request):
    num1 = 10
    num2 = 10
    result = num1 + num2
    return HttpResponse(f"soma: {result}")
