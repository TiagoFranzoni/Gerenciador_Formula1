from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from pilotos.models import Pilotos
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import FormPilotos, FormLogin, FormNovoUsuario
from django.template import RequestContext
from django.contrib import messages
from django.urls import reverse
from .models import Pilotos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import PilotosSerializer
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.db import connection
from django.views import View


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Home(View):
    """docstring"""
    template_name = 'pilotos/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        return render(request, 'pilotos/home.html', self.context)


class PilotosView(ListView):
    """docstring"""
    model = Pilotos
    template_name = 'pilotos/pilotos_archive.html'
    context_object_name = 'piloto'

class PilotosList(generics.ListCreateAPIView):
    """docstring"""
    permission_classes = [IsAuthenticated]
    queryset = Pilotos.objects.all()
    serializer_class = PilotosSerializer

class PilotosViewDetail(DetailView):
    """docstring"""
    model = Pilotos
    template_name = 'pilotos/pilotos_detail.html'
    context_object_name = 'piloto'


class PilotosViewAdiciona(View):
    """docstring"""
    template_name = 'pilotos/cria_piloto.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormPilotos()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormPilotos(request.POST)
        if form.is_valid():
            nome_piloto = form.cleaned_data.get('nome')
            if Pilotos.objects.filter(nome=nome_piloto).exists():
                messages.warning(request, f'Já existe um cadastro: "{nome_piloto}".')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect('/view/pilotos')
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class PilotosViewEdita(UpdateView):
    """docstring"""
    model = Pilotos
    form_class = FormPilotos
    template_name = 'pilotos/edita_piloto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['piloto'] = self.object
        return context

    def get_success_url(self):
        return '/view/pilotos'


class PilotosViewExclui(View):
    """docstring"""
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormPilotos()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        if not request.user.has_perm('pilotos.can_delete_piloto'):
            messages.error(request, "Você não tem permissão para deletar Pilotos.")
            return redirect('/view/pilotos')
        piloto = Pilotos.objects.get(pk=kwargs['pk'])
        piloto.delete()
        return redirect('/view/pilotos')

    def delete(self, request, *args, **kwargs):
        """docstring"""
        if not request.user.has_perm('pilotos.can_delete_piloto'):
            messages.error(request, "Você não tem permissão para deletar Pilotos.")
            return redirect('/view/pilotos')
        piloto = Pilotos.objects.get(pk=kwargs['pk'])
        piloto.delete()
        return redirect('/view/pilotos')


class PilotosDetailList(generics.RetrieveUpdateDestroyAPIView):
    """docstring"""
    queryset = Pilotos.objects.all()
    serializer_class = PilotosSerializer


class ResetDbPilotos(View):
    """docstring"""
    def get(self, request):
        """docstring"""
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM pilotos_pilotos;")
            cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'pilotos_pilotos';")
        return HttpResponse("Tabela Pilotos resetada.")
