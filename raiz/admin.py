from django.contrib import admin

# Importando os models criado
from .models import Contato, Categoria


class ContatosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'categoria')


class CategAdmin(admin.ModelAdmin):
    list_display = ('id','nome')


# Mostra na area admin os dados das class
admin.site.register(Categoria, CategAdmin)
admin.site.register(Contato, ContatosAdmin)

