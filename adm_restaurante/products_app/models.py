from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    preco_produto = models.FloatField()
    desc_produto = models.CharField(max_length=200)
    categoria_produto = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto
