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
from django.http import HttpResponse
from django.db import connection
from django.views import View


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarrosView(ListView):
    """docstring"""
    model = Carros
    template_name = 'carros/carros_archive.html'
    context_object_name = 'carro'

class CarrosList(generics.ListCreateAPIView):
    """docstring"""
    permission_classes = [IsAuthenticated]
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer

class CarrosViewDetail(DetailView):
    """docstring"""
    model = Carros
    template_name = 'carros/carros_detail.html'
    context_object_name = 'carro'


class CarrosViewAdiciona(View):
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
                messages.warning(request, f'Já existe um cadastro: "{nome_carro}".')
                self.context['form'] = form
                return render(request, self.template_name, self.context)
            form.save()
            return redirect('/view/carros')
        self.context['form'] = form
        return render(request, self.template_name, self.context)


class CarrosViewEdita(UpdateView):
    """docstring"""
    model = Carros
    form_class = FormCarros
    template_name = 'carros/edita_carro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carro'] = self.object
        return context

    def get_success_url(self):
        return '/view/carros'


class CarrosViewExclui(View):
    """docstring"""
    context = {}

    def get(self, request, *args, **kwargs):
        """docstring"""
        self.context['form'] = FormCarros()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        """docstring"""
        if not request.user.has_perm('carros.can_delete_carro'):
            messages.error(request, "Você não tem permissão para deletar Carros.")
            return redirect('/view/carros')
        carro = Carros.objects.get(pk=kwargs['pk'])
        carro.delete()
        return redirect('/view/carros')

    def delete(self, request, *args, **kwargs):
        """docstring"""
        if not request.user.has_perm('carros.can_delete_carro'):
            messages.error(request, "Você não tem permissão para deletar Carros.")
            return redirect('/view/carros')
        carro = Carros.objects.get(pk=kwargs['pk'])
        carro.delete()
        return redirect('/view/carros')


class CarrosDetailList(generics.RetrieveUpdateDestroyAPIView):
    """docstring"""
    queryset = Carros.objects.all()
    serializer_class = CarrosSerializer


class ResetDbCarros(View):
    """docstring"""
    def get(self, request):
        """docstring"""
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM carros_carros;")
            cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'carros_carros';")
        return HttpResponse("Tabela Carros resetada.")
