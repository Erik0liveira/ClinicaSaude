from django.urls import path
from .views import IndexView, SobreView, ServicoView, ContatoView

urlpatterns = [
     path('', IndexView.as_view(), name='inicio'), 
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('servicos/', ServicoView.as_view(), name='servicos'),
    path('contatos/', ContatoView.as_view(), name='contatos')
]
