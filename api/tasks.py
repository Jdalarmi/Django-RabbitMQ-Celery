from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Emprestimo

@shared_task
def add(proposta_id):
    print('_________INICIANDO ANALISE__________')
    proposta = Emprestimo.objects.get(pk=proposta_id)
    if proposta.valor_emprestimo > 1000:
        proposta.status = "APROVADO"
    else:
        proposta.status = "NEGADO"

    proposta.save()

    print(f"recebido a task do emprestimo ID{proposta.id}")
    
    return proposta.id