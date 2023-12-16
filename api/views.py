from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


@swagger_auto_schema(method='post')
@api_view(['POST'])
def register(request):
    ...