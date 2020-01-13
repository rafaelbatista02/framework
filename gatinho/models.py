from django.db import models

# Create your models here.
from dono.models import Dono


class Gatinho(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cores = (
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('PARDO', 'Pardo'),
    )
    cor = models.CharField(choices=cores, max_length=100)
    dono = models.ManyToManyField(Dono, null=True)