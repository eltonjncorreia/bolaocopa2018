from django.shortcuts import render

from copa.core.models import Jogo, Grupo, Selecao


def home(request):
    jogo = Jogo.objects.all()
    return render(request, 'core/index.html', {'jogos': jogo})


def grupo(request):
    lista = []
    grupo = Grupo.objects.all()
    for g in grupo:
        selecao = Selecao.objects.all().filter(grupo__nome_grupo=g)
        lista.append(selecao)
    context = {
        'grupo_a': lista,

    }

    return render(request, 'core/grupos.html', context)















