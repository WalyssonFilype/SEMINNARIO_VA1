from django.db import models

class detalhe_turma(models.Model):
    codigoAluno = models.IntegerFieldInter()
    codigoProfessor = models.IntegerField()
    codigoTurma = models.IntegerField()