""""Docstring"""
from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from pilotos.models import Pilotos

# Register your models here.
class PilotosAdmin(ModelAdmin):
    """Docstring"""
    fields = ['nome', 'data_de_nascimento', 'nacionalidade', 'detalhes', 'ativo']
    list_display = ['nome', 'data_de_nascimento', 'nacionalidade', 'detalhes', 'ativo']
    list_editable = ['ativo']

site.register(Pilotos, PilotosAdmin)