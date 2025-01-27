from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('servico/', views.cadastro_servico, name='cadastro_servico'),
    path('profissional/', views.cadastro_profissional, name='cadastro_profissional'),
]
