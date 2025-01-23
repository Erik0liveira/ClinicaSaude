
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class ServicoView(TemplateView):
    template_name = "paginas/servico.html"

class ContatoView(TemplateView):
    template_name = "paginas/contato.html"