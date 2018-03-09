from django.shortcuts import render

from copa.core.models import Jogo, Aposta
from copa.usuario.views import create_users, empty_form


def home(request):
    jogo = Jogo.objects.all()

    return render(request, 'core/index.html', {'jogos': jogo})















