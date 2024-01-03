from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Emprestimo
import random

@shared_task
def avaliar_proposta(proposta_id):
    print('_________INICIANDO ANALISE__________')
    proposta = Emprestimo.objects.get(pk=proposta_id)

    if random.choice([True, False]):
        proposta.status = "APROVADO"
    else:
        proposta.status = "NEGADO"

    proposta.save()

    print(f"recebido a task do emprestimo ID{proposta.id}")
    
    return proposta.id