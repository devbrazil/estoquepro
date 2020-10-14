from django.shortcuts import render
from .models import Equipamento

def index(request):

    produtos = Equipamento.objecjs.all()
    context = {
    'equipamentos': produtos
    }
    return render(request, 'index.html', context)
# def estoque_geral(request):
#     return render(request, 'estoque_geral.html')
