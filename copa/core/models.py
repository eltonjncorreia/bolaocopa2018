from django.db import models


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome_grupo


class Selecao(models.Model):

    nome = models.CharField(max_length=255,  null=True)
    sigla = models.CharField(max_length=4, blank=True, null=True)
    slug = models.SlugField(null=True)
    gol_marc = models.IntegerField(default=0, null=True, blank=True,)
    gol_sofr = models.IntegerField(null=True, blank=True,)
    pontos = models.IntegerField(null=True, blank=True,)
    bandeira = models.ImageField(upload_to='media', null=True, blank=True,)
    grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE, related_name='grupos')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Seleção'
        verbose_name_plural = 'Seleções'

    def __str__(self):
        return self.nome




class Jogo(models.Model):
    horario = models.DateTimeField(auto_now_add=False)
    selecao_1 = models.ForeignKey('Selecao', on_delete=models.CASCADE, related_name='selecoes_1')
    selecao_2 = models.ForeignKey('Selecao',on_delete=models.CASCADE, related_name='selecoes_2')
    placar_1 = models.CharField(max_length=2, blank=True, null=True)
    placar_2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        ordering = ('horario',)

    def __str__(self):
        return str(self.selecao_1) + " x " + str(self.selecao_2)


class Aposta(models.Model):
    user_da_aposta = models.ForeignKey('auth.User', related_name='user_da_apostas', on_delete=models.CASCADE)
    jogo = models.ForeignKey('Jogo', related_name='jogos', on_delete=models.CASCADE)
    placar_1 = models.CharField(max_length=2)
    placar_2 = models.CharField(max_length=2)
    preco = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.jogo)




