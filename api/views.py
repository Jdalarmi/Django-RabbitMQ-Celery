from django.http import HttpResponse
from rest_framework.response import Response 
from rest_framework import viewsets
from .models import Emprestimo
from .serializers import EmprestimoSerializer
from .tasks import avaliar_propostas
from rest_framework import status


class PropostaViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()

        avaliar_propostas.apply_async()

        return HttpResponse({'status': 'Proposta criada com sucesso. Avaliação em andamento.'}, status=status.HTTP_201_CREATED)