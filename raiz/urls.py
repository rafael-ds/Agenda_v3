from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('sair/', views.sair, name='sair'),
    path('novoContato/', views.novoContato, name='novoContato'),
    path('busca/', views.busca, name='busca'),
    path('<int:contato_id>/', views.contato, name='contato'),# mostrando um unico contato
    path('delete/<int:id>', views.delete, name='delete'),
    # path('editar/<int:id>', views.editar, name='editar'),
]