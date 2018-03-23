from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, resolve_url as r

from copa.core.models import Jogo, Grupo, Selecao


def home(request):
    jogo = Jogo.objects.all().order_by('horario')
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


def aposta(request, jogo_id):

    try:
        jogo_id = get_object_or_404(Jogo, pk=jogo_id)
    except Jogo.DoesNotExist:
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': jogo_id,
            'error_message': "You didn't select a choice.",
        })
    # else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    # return HttpResponseRedirect(r('core:home'))
    return render(request, 'core/apostas.html', {'id': jogo_id})












