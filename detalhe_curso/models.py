from django.db import models

class detalhe_curso(models.Model):
    codigoCurso = models.IntegerField()
    codigoTurma = models.IntegerField()