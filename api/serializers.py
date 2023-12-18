from rest_framework import serializers
from .models import Emprestimo, CampoProposta

class CampoPropostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoProposta
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    campos = CampoPropostaSerializer(many=True, read_only=True)

    class Meta:
        model = Emprestimo
        fields = '__all__'