from django.urls import path
from .import views
urlpatterns = [
    path('', views.acess_proposta, name='acess-emprestimo'),
    path('find_protocol', views.find_protocol, name="find-protocol")
    
]