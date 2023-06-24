from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    matricula = models.IntegerField()
    dataNascimento = models.IntegerField()    


    def __str__(self):
      return self.nome
