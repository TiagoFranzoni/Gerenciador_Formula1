"""Docstring"""
from rest_framework import serializers
from .models import Equipes

class EquipesSerializer(serializers.ModelSerializer):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Equipes
        fields = '__all__'
