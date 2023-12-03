"""Docstring"""
from django.forms import ModelForm
from .models import Carros

class FormCarros(ModelForm):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Carros
        fields = ['nome', 'modelo', 'equipe']
