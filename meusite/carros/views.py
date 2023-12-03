"""docstring"""
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from carros.models import Carros
from django.views.generic import View
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.urls import reverse
from .models import Carros
from .forms import FormCarros
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CarrosSerializer
from django.views.generic.list import ListView


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Home(View):
    """docstring"""
    template_name = 'carros/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        return render(request, 'carros/home.html', self.context)


class CarrosView(ListView):
    """docstring"""
    model = Carros
    date_field = 'data_de_criacao'
    template_name = 'carros/carros_archive.html'

class CarrosList(generics.ListCreateAPIView):
    """docstring"""
    permission_classes = [IsAuthenticated]
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


# class CarrosDetail(DetailView):
#     """docstring"""
#     model = Carros
#     template_name = 'carros/carros_detail.html'
#     context_object_name = 'carros'

class CarrosDetail(generics.RetrieveUpdateDestroyAPIView):
    """docstring"""
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


class AdicionaCarros(View):
    """docstring"""
    template_name = 'carros/cria_carro.html'
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormCarros()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        form = FormCarros(request.POST)
        if form.is_valid():
            nome_carro = form.cleaned_data.get('nome')
            if Carros.objects.filter(nome=nome_carro).exists():
                messages.error(request, f'Já existe um Carro com o nome "{nome_carro}".')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect('/carros/')
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class EditaCarros(UpdateView):
    """docstring"""
    model = Carros
    form_class = FormCarros
    template_name = 'carros/edita_carros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carro'] = self.object
        return context

    def get_success_url(self):
        return '/carros/'


class ExcluiCarros(View):
    """docstring"""
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormCarros()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        carro = Carros.objects.get(pk=kwargs['pk'])
        carro.delete()
        return redirect('/carros/')
