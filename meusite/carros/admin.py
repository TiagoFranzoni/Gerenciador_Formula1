""""Docstring"""
from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from carros.models import Carros

# Register your models here.
class CarrosAdmin(ModelAdmin):
    """Docstring"""
    fields = ['nome', 'modelo', 'detalhes', 'em_uso']
    list_display = ['nome', 'modelo', 'detalhes', 'em_uso']
    list_editable = ['em_uso']

site.register(Carros, CarrosAdmin)