from django.shortcuts import render

# Create your views here.
def cadastro_cliente(request):
    return render(request, 'cadastro/cadastro_cliente.html')

def cadastro_servico(request):
    return render(request, 'cadastro/cadastro_servico.html')

def cadastro_profissional(request):
    return render(request, 'cadastro/cadastro_profissional.html')