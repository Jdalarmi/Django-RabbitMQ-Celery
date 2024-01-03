from rest_framework.response import Response 
from .serializers import EmprestimoSerializer
from .tasks import add
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=EmprestimoSerializer)
@api_view(['POST'])
def acess_proposta(request):
    serializer = EmprestimoSerializer(data=request.data)

    if serializer.is_valid():
        proposta = serializer.save()
        add.delay(proposta.id)
        return Response('Sua Proposta foi recebida com sucesso e esta em processo de avaliação por favor aguarde!!!')
    else:
        return Response(serializer.errors)