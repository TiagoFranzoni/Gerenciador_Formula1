"""Docstring"""
from rest_framework import serializers
from .models import Carros

class CarrosSerializer(serializers.ModelSerializer):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Carros
        fields = '__all__'