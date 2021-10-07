from django.urls import path
from django.urls import path

from .views import index, cadastro, home, sair, novoContato

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('home/', home, name='home'),
    path('sair/', sair, name='sair'),
    path('novoContato/', novoContato, name='novoContato'),
]