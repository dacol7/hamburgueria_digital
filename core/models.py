from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(AbstractUser):
    idade = models.PositiveIntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

class Hamburguer(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='hamburgueres/', null=True, blank=True)

    def __str__(self):
        return self.nome    