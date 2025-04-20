from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    Sobrenome = models.CharField(max_length=35)
    cpf_cliente = models.CharField(max_length=11)
    genero = models.CharField(max_length=30)
    estado_civil = models.CharField(max_length=20)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    data_hora_cadastro = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.nome} {self.Sobrenome}'
    
    


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return f'Cidade: {self.cidade} | Cliente: {self.cliente.nome}'
