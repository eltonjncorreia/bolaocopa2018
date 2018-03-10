from django.shortcuts import render

from copa.core.models import Jogo, Aposta, Grupo, Selecao
from copa.usuario.views import create_users, empty_form


def home(request):
    jogo = Jogo.objects.all()
    return render(request, 'core/index.html', {'jogos': jogo, 'grupo': grupo})


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















