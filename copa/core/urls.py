from django.urls import path
from copa.core.views import home, grupo, aposta, minha_aposta

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('grupos/', grupo, name='grupo'),
    path('minhas-apostas/', minha_aposta, name='minha_aposta'),
    path('<int:jogo_id>/aposta/', aposta, name='aposta'),
]
