from django.urls import path
from copa.core.views import home, grupo, aposta

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('grupos/', grupo, name='grupo'),
    path('<int:jogo_id>/aposta/', aposta, name='aposta'),
]
