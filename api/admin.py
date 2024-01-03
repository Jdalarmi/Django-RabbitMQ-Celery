from django.contrib import admin

from django.contrib import admin
from .models import Emprestimo

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('id',  'status')

admin.site.register(Emprestimo, PropostaAdmin)
