from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from api.tasks import process_emprestimo_message
from core import settings
from .serializers import EmprestimoSerializer
import json
import pika
from .models import StatusEmprestimo

@swagger_auto_schema(method='post', request_body=EmprestimoSerializer)
@api_view(['POST'])
def register(request):
    serializer = EmprestimoSerializer(data=request.data)
    if serializer.is_valid():
       
      
        emprestimo = serializer.save()

          
        json_parameters = json.dumps({
            'emprestimo_id': emprestimo.id,
            'emprestimo_nome':emprestimo.nome,
            'emprestimo_cpf':emprestimo.cpf,
            'emprestimo_endereco':emprestimo.endereco,
            'emprestimo_valor': emprestimo.valor_do_emprestimo
                
            })
    
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=pika.PlainCredentials(
                settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD
            )
        ))
        channel = connection.channel()

        channel.basic_publish(
            exchange='proposta_avaliable',
            routing_key='proposta',
            body=json_parameters
        )

        value_for_status = process_emprestimo_message(json_parameters)
        if value_for_status > 1000:
            StatusEmprestimo.objects.create(
                status='APROVADO'
            )
        else:
            StatusEmprestimo.objects.create(
                status='NEGADO'
            )

        connection.close()
        return Response('Dados salvos com sucesso e Enviados para fila proposta', status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
