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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Home(View):
    """docstring"""
    template_name = 'pilotos/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        return render(request, 'pilotos/home.html', self.context)


class PilotosView(ArchiveIndexView):
    """docstring"""
    model = Pilotos
    date_field = 'data_de_criacao'
    template_name = 'pilotos/pilotos_archive.html'

class PilotosList(generics.ListCreateAPIView):
    """docstring"""
    permission_classes = [IsAuthenticated]
    queryset = Pilotos.objects.all()
    serializer_class = PilotosSerializer


# class PilotosDetail(DetailView):
#     """docstring"""
#     model = Pilotos
#     template_name = 'pilotos/pilotos_detail.html'
#     context_object_name = 'pilotos'

class PilotosDetail(generics.RetrieveUpdateDestroyAPIView):
    """docstring"""
    queryset = Pilotos.objects.all()
    serializer_class = PilotosSerializer


class AdicionaPilotos(View):
    """docstring"""
    template_name = 'pilotos/cria_pilotos.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormPiloto()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormPiloto(request.POST)
        if form.is_valid():
            nome_epiloto = form.cleaned_data.get('nome')
            if Pilotos.objects.filter(nome=nome_epiloto).exists():
                messages.error(request, f'Uma biblioteca com o nome "{nome_epiloto}" já existe.')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect('/pilotos/')
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class EditaPilotos(UpdateView):
    """docstring"""
    model = Pilotos
    form_class = FormPilotos
    template_name = 'pilotos/edita_pilotos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['piloto'] = self.object
        return context

    def get_success_url(self):
        return '/pilotos/'


class ExcluiPilotos(View):
    """docstring"""
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormPilotos()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        piloto = Pilotos.objects.get(pk=kwargs['pk'])
        piloto.delete()
        return redirect('/pilotos/')
