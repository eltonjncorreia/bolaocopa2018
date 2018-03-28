from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url as r
from copa.core.models import Jogo, Grupo, Selecao, Aposta
# from datetime import date


def home(request):
    # hoje = date.today().day
    # jogo = Jogo.objects.filter(horario__day=15).order_by('horario')
    jogo = Jogo.objects.all().order_by('horario')
    contexto = {
        'jogos': jogo
    }
    return render(request, 'core/home.html', contexto)


def grupo(request):
    lista = []
    grupo = Grupo.objects.all().order_by('nome_grupo')
    for g in grupo:
        selecao = Selecao.objects.all().filter(grupo__nome_grupo=g)
        lista.append(selecao)

    context = {
        'grupo_a': lista,

    }

    return render(request, 'core/grupos.html', context)


def aposta(request, jogo_id):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':

        jogo = Jogo.objects.get(pk=jogo_id)
        placa1 = request.POST.get('placar1')
        placa2 = request.POST.get('placar2')
        preco = request.POST.get('preco')

        Aposta.objects.create(user_da_aposta=user,
                              jogo=jogo,
                              placar_1=placa1,
                              placar_2=placa2,
                              preco=preco)

        messages.success(request, 'Aposta realizada')
        return HttpResponseRedirect(r('core:home'))
    else:
        return HttpResponseRedirect(r('core:erro_aposta'))




def minha_aposta(request):

    aposta = Aposta.objects.all().filter()
    return render(request, 'core/minhas_apostas.html', {'apostas': aposta})







