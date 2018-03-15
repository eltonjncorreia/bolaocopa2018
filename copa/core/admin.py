from django.contrib import admin

# Register your models here.
from copa.core.models import Selecao, Jogo, Aposta, Grupo


class ApostaInlines(admin.StackedInline):
    model = Aposta
    extra = 1


class JogoAdmin(admin.ModelAdmin):
    list_display = ['horario', 'selecao_1', 'placar_1', 'placar_2', 'selecao_2']


class ApostaAdmin(admin.ModelAdmin):
    list_display = ['jogo', 'placar_1', 'placar_2', 'preco']


class SelecaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'grupo', 'bandeira']


admin.site.register(Selecao, SelecaoAdmin)
admin.site.register(Grupo)
admin.site.register(Aposta, ApostaAdmin)
admin.site.register(Jogo, JogoAdmin)
