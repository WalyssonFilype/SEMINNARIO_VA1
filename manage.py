#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from aluno.models import models

from aluno.AlunoSerializers import AlunoSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

models = models(nome='Paul', sexo='Van Dyke', matricula="")
models.save()

models = models(nome='Regis', sexo='Santos', matricula="")
models.save()

serializer = AlunoSerializers(models)
serializer.data

content = JSONRenderer().render(serializer.data)
content

