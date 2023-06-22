from django.db import models

class turma(models.Model):
    codigo = models.IntegerField()
    codigoCurso = models.IntegerField()