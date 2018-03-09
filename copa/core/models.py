from django.db import models
from django.shortcuts import resolve_url as r


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=1)

    def __str__(self):
        return self.nome_grupo


class Selecao(models.Model):
    nome = models.CharField(max_length=255, null=True)
    sigla = models.CharField(max_length=4, null=True)
    slug = models.SlugField()
    grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE, related_name='grupos')


    class Meta:
        verbose_name = 'Seleção'
        verbose_name_plural = 'Seleções'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return r('speaker-detail', slug=self.slug)


class Jogo(models.Model):
    horario = models.DateField(auto_now=True)
    selecao_1 = models.ForeignKey('Selecao', on_delete=models.CASCADE, related_name='selecoes_1')
    selecao_2 = models.ForeignKey('Selecao',on_delete=models.CASCADE, related_name='selecoes_2')
    placar_1 = models.CharField(max_length=2, blank=True)
    placar_2 = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return str(self.selecao_1) + " x " + str(self.selecao_2)


class Aposta(models.Model):
    jogo = models.ForeignKey('Jogo', related_name='jogos', on_delete=models.CASCADE)
    placar_1 = models.CharField(max_length=2)
    placar_2 = models.CharField(max_length=2)
    DOIS = '2'
    CINCO = '5'
    DEZ = '10'
    VINTE = '20'

    PRECO = ((DOIS, '2'),
             (CINCO, '5'),
             (DEZ, '10'),
             (VINTE, '20'))

    preco = models.CharField(max_length=1, choices=PRECO)

    def __str__(self):
        return str(self.jogo)




