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
    dono = models.ManyToManyField(Dono, null=True)


