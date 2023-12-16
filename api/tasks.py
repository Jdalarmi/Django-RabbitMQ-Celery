from celery import shared_task
import json

@shared_task
def processar_emprestimo(parametros_json):
    parametros = json.loads(parametros_json)
    print(f'Parâmetros recebidos: {parametros}')

