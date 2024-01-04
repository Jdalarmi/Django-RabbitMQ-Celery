from rest_framework.response import Response 
from .serializers import EmprestimoSerializer
from .models import Protocol, Emprestimo
from .tasks import avaliar_proposta
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
import string
from random import SystemRandom

def random_letters(k=10):
    return SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k
    )

@swagger_auto_schema(method='post', request_body=EmprestimoSerializer)
@api_view(['POST'])
def acess_proposta(request):
    random_string = ''.join(random_letters())
    data = Protocol.objects.create(
        protocol = random_string
    )
    serializer = EmprestimoSerializer(data=request.data)
    if serializer.is_valid():
        proposta = serializer.save()

        avaliar_proposta.delay(proposta.id)
    
        return Response(f'Sua Proposta foi recebida com sucesso e esta em processo de avaliação. Seu protocolo: {data.protocol} Status da proposta: {data.status}')
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
def find_protocol(request):
    if request.method == 'GET':
        data = Protocol.objects.all()
        for i in data:
            data = i 
        return Response(f"Segue a lista do protocolos com status após avaliação. Seu protocolo: {data.protocol}  Novo Status da proposta: {data.status}")