# tasks.py
from celery import shared_task
import json
from .models import Emprestimo, StatusEmprestimo

@shared_task(queue='proposta')
def process_emprestimo_message(message):
    try:
        data = json.loads(message)
        emprestimo_valor = data.get('emprestimo_valor')
        return emprestimo_valor
    except Exception as e:
        return None
