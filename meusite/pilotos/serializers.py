"""Docstring"""
from rest_framework import serializers
from .models import Pilotos

class PilotosSerializer(serializers.ModelSerializer):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Pilotos
        fields = '__all__'