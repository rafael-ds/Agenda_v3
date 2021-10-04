from django.urls import path
from django.urls import path

from .views import index, cadastro, home

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('home/', home, name='home'),
]