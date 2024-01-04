from django.contrib import admin

from django.contrib import admin
from .models import Emprestimo, Protocol

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('id',  'status')
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('protocol', 'status')
admin.site.register(Emprestimo, PropostaAdmin)
admin.site.register(Protocol, ProtocolAdmin)
