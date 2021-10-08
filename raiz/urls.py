from django.urls import path
from django.urls import path

from .views import index, cadastro, home, sair, novoContato, contato, busca

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('home/', home, name='home'),
    path('sair/', sair, name='sair'),
    path('novoContato/', novoContato, name='novoContato'),
    path('busca/', busca, name='busca'),
    path('<int:contato_id>/', contato, name='contato'),# mostrando um unico contato
]