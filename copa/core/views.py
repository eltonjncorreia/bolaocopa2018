from django.shortcuts import render

from copa.core.models import Jogo, Aposta, Grupo, Selecao
from copa.usuario.views import create_users, empty_form


def home(request):
    jogo = Jogo.objects.all()
    return render(request, 'core/index.html', {'jogos': jogo, 'grupo': grupo})


def grupo(request):
    grupo_a = Selecao.objects.filter(grupo__nome_grupo='A').order_by('nome')

    context = {
        'grupo_a': grupo_a,

    }

    return render(request, 'core/grupos.html', context)















