from django.db import models
from django import forms
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=50)

    def __str__(self) -> str:
        return self.nome
    

class Contato(models.Model):
    nome = models.CharField('Nome', max_length=80)
    telefone = models.CharField('Telefone', max_length=25)
    email = models.EmailField('E-mail', max_length=100, blank=True)
    data_regis = models.DateTimeField('DataRegistro', auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)

    def __str__(self) -> str:
        return self.nome


