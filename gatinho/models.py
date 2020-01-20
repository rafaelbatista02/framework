from django.db import models

# Create your models here.
from dono.models import Dono



class Gatinho(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cor_da_pele = (
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('LARANJA', 'Laranja'),
        ('CINZA', 'Cinza'),
        ('TRICOLOR', 'Tricolor'),
        ('BEGE', 'Bege'),
    )
    cor = models.CharField(choices=cor_da_pele, max_length=100)
    dono = models.ManyToManyField(Dono, blank=True)

def __str__(self):
    return self.nome

class Anuncio(models.Model):
    nome_da_empresa = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone =  models.CharField(max_length=15)
    valor = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    



