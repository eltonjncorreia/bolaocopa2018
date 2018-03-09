from django.contrib import admin

# Register your models here.
from copa.core.models import Selecao, Jogo, Aposta


class ApostaInlines(admin.StackedInline):
    model = Aposta
    extra = 1


class JogoAdmin(admin.ModelAdmin):
    list_display = ['horario', 'selecao_1', 'placar_1', 'placar_2', 'selecao_2']


class ApostaAdmin(admin.ModelAdmin):
    list_display = ['jogo', 'placar_1', 'placar_2', 'preco']


admin.site.register(Selecao)
admin.site.register(Aposta, ApostaAdmin)
admin.site.register(Jogo, JogoAdmin)
