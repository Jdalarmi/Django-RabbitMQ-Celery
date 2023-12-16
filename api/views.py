from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .serializers import EmprestimoSerializer
from api.tasks import processar_emprestimo
import json

@swagger_auto_schema(method='post', request_body=EmprestimoSerializer)
@api_view(['POST'])
def register(request):
    serializer = EmprestimoSerializer(data=request.data)

    if serializer.is_valid():
       
        with transaction.atomic():
            emprestimo = serializer.save()

          
            parametros_json = json.dumps({
                'emprestimo_id': emprestimo.id,
                
            })
            print(f'Parâmetros JSON: {parametros_json}')

            processar_emprestimo.apply_async(args=[parametros_json], queue="emprestimos")
            print(f'Tarefa enviada para processar empréstimo. ID do empréstimo: {emprestimo.id}')

        return Response('Dados salvos com sucesso', status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)