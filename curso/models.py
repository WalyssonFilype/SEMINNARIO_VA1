from django.db import models

class curso(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
   

