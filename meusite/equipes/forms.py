"""Docstring"""
from django.forms import Form
from django.forms import CharField
from django.forms import EmailField
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Equipes

class FormEquipes(ModelForm):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Equipes
        fields = ['nome', 'fundador', 'administrador', 'detalhes', 'ativa']

class FormLogin(Form):
    """Docstring"""
    nome_de_usuario = CharField()
    senha = CharField(widget=PasswordInput)

    def autentica(self, request):
        """Docstring"""
        username = self.cleaned_data['nome_de_usuario']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise ValidationError("Dados de login inválidos.")
        login(request, user)



class FormNovoUsuario(Form):
    """Docstring"""
    nome_de_usuario = CharField(required=True)
    nome = CharField(required=False)
    email = EmailField(required=False)
    senha = CharField(widget=PasswordInput)
    repeticao_senha = CharField(widget=PasswordInput)

    def save(self):
        """Docstring"""
        params = {
            'username': self.cleaned_data['nome_de_usuario'], 
            'email': self.cleaned_data['email'],
            # 'password': self.cleaned_data['senha'],
        }
        if self.cleaned_data['nome']:
            params['first_name'] = self.cleaned_data['nome']
        password = self.cleaned_data['senha']
        User.objects.create_user(password=password, **params)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        repeticao_senha = cleaned_data.get('repeticao_senha')

        if senha and repeticao_senha and senha != repeticao_senha:
            raise ValidationError("As senhas devem ser iguais.")

        return cleaned_data
