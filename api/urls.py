from django.urls import path
from .import views
urlpatterns = [
    path('', views.acess_proposta, name='acess-emprestimo'),
    
]