"""docstring"""
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from equipes.models import Equipes
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import FormEquipes, FormLogin, FormNovoUsuario
from django.template import RequestContext
from django.contrib import messages
from django.urls import reverse
from .models import Equipes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import EquipesSerializer
from django.views.generic.list import ListView


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Home(View):
    """docstring"""
    template_name = 'equipes/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        return render(request, 'equipes/home.html', self.context)


class EquipesView(ListView):
    """docstring"""
    model = Equipes
    template_name = 'equipes/equipes_archive.html'
    context_object_name = 'equipes'

class EquipesList(generics.ListCreateAPIView):
    """docstring"""
    permission_classes = [IsAuthenticated]
    queryset = Equipes.objects.all()
    serializer_class = EquipesSerializer


# class EquipesDetail(DetailView):
#     """docstring"""
#     model = Equipes
#     template_name = 'equipes/equipes_detail.html'
#     context_object_name = 'equipes'

class EquipesDetail(generics.RetrieveUpdateDestroyAPIView):
    """docstring"""
    queryset = Equipes.objects.all()
    serializer_class = EquipesSerializer


class AdicionaEquipes(View):
    """docstring"""
    template_name = 'equipes/cria_equipe.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormEquipes()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormEquipes(request.POST)
        if form.is_valid():
            nome_equipe = form.cleaned_data.get('nome')
            if Equipes.objects.filter(nome=nome_equipe).exists():
                messages.error(request, f'Uma biblioteca com o nome "{nome_equipe}" já existe.')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect('/equipes/list/')
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class EditaEquipes(UpdateView):
    """docstring"""
    model = Equipes
    form_class = FormEquipes
    template_name = 'equipes/edita_equipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipe'] = self.object
        return context

    def get_success_url(self):
        return '/equipes/list/'


class ExcluiEquipes(View):
    """docstring"""
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormEquipes()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        equipe = Equipes.objects.get(pk=kwargs['pk'])
        equipe.delete()
        return redirect('/equipes/list/')

    def delete(self, request, *args, **kwargs):
        """docstring"""
        equipe = Equipes.objects.get(pk=kwargs['pk'])
        equipe.delete()
        return redirect('/equipes/list/')


class Login(View):
    """docstring"""
    template_name = 'login_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormLogin()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('nome_de_usuario')
            password = form.cleaned_data.get('senha')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            messages.warning(request, 'Nome de usuário ou senha inválidos')
        self.context['form'] = form
        return render(request, self.template_name, self.context)



    def clean(self):
        """docstring"""
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class CriaUsuario(View):
    """docstring"""
    template_name = 'criar_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormNovoUsuario()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('nome_de_usuario')
            password = form.cleaned_data.get('senha')
            first_name = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            # user = User.objects.create_user(username=username, password=password)
            user = User.objects.create_user(username=username, first_name=first_name, email=email)
            user.set_password(password)
            user.save()
            # login(request, user)
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('/login/')
        self.context['form'] = form
        return render(request, self.template_name, self.context)

