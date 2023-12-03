"""Docstring"""
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('equipes.urls', 'equipes'), namespace='equipes')),
    path('logout/', auth_views.LogoutView.as_view(next_page='equipes:equipes-home'), name='logout'),

    path('carros/', include(('carros.urls', 'carros'), namespace='carros')),
    path('pilotos/', include(('pilotos.urls', 'pilotos'), namespace='pilotos')),

    path('api/', include(('equipes.urls', 'api-equipes'), namespace='api-equipes')),
    path('api/carros/', include(('carros.urls', 'api-carros'), namespace='api-carros')),
    path('api/pilotos/', include(('pilotos.urls', 'api-pilotos'), namespace='api-pilotos')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
