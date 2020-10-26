from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Equipamento


@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


def list_estoque(request):
    equipametos = Equipamento.objects.filter()
    return render(request, 'estoque.html', {'equipamento': equipametos})


def logout_user(request):
    logout(request)
    return redirect('/login/')

@csrf_protect
def login_user(request):
    return render(request, 'login.html')

"""
a função submit_login recebe os dados do template e valida se o usuário e senha estão corretos,
caso esteja errado ele envia uma mensagem para o template informando o erro.
"""


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Usuário ou Senha Inválido. Favor tentar novamente')
    return redirect('/login/')

