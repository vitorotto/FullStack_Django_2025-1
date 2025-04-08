from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("categoria_produto", "nome_produto", "preco_produto",)
    list_filter = ("categoria_produto",)
