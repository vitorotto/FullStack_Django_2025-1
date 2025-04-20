from django.contrib import admin
from .models import Cliente, Endereco

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'Sobrenome', 'cpf_cliente', 'genero', 'estado_civil', 'telefone', 'email', 'data_hora_cadastro',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep',)
    list_filter = ('cidade', 'estado',)
