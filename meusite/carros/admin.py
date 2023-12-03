""""Docstring"""
from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from carros.models import Carros

# Register your models here.
class CarrosAdmin(ModelAdmin):
    """Docstring"""
    fields = ['nome', 'modelo', 'detalhes', 'ativo']
    list_display = ['nome', 'modelo', 'detalhes', 'ativo']
    list_editable = ['ativo']

site.register(Carros, CarrosAdmin)