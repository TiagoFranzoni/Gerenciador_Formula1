""""Docstring"""
from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from equipes.models import Equipes

# Register your models here.
class EquipesAdmin(ModelAdmin):
    """Docstring"""
    fields = ['nome', 'detalhes', 'fundador', 'administrador', 'ativa']
    list_display = ['nome', 'detalhes', 'fundador', 'administrador', 'ativa']
    list_editable = ['ativa']

site.register(Equipes, EquipesAdmin)
