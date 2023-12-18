# tasks.py
from celery import shared_task
from .models import Emprestimo

@shared_task(
        bind=True,
        max_retries=5,
        default_retry_delay=30)

def avaliar_propostas():
    print("Iniciando a avaliação de propostas...")
    
    propostas = Emprestimo.objects.filter(status='Aguardando')
    aprovacao = True
    
    for proposta in propostas:
        print(f"Avaliando proposta ID {proposta.id}...")
        proposta.status = 'Aprovada' if aprovacao else 'Negada'
        proposta.save()
        aprovacao = not aprovacao
    
    print("Concluída a avaliação de propostas.")
