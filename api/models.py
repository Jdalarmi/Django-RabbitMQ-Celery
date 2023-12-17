from django.db import models

class Emprestimo(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=100, null=False)
    valor_do_emprestimo = models.FloatField(null=True)

class StatusEmprestimo(models.Model):
    status_choices =(
        ('1', 'Aprovado'),
        ('2', 'Negado')
    )
    # emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_choices)