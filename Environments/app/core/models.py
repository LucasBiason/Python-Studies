from django.db import models

class Estoque(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=130)
    quantidade = models.IntegerField()
