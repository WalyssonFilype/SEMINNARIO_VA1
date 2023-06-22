from django.db import models

class disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

