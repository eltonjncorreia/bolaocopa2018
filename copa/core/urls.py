from django.urls import path
from copa.core.views import home, grupo

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('grupos/', grupo, name='grupo'),
]
