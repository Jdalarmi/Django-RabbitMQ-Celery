from rest_framework import serializers
from .models import Emprestimo

class EmprestimoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emprestimo
        exclude= ['status']