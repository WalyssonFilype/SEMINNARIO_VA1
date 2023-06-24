from rest_framework  import serializers
from .models import aluno

class AlunoSerializers(serializers.models):
    class Meta: 
        model = aluno
        fields = [
            'name' 
            'sexo' 
            'matricula'
            'dataNascimento'
        ]