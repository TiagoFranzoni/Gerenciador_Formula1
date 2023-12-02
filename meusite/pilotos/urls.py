"""docstring"""
from django.urls import path
from pilotos.views import PilotosDetail, Home, AdicionaPilotos, ExcluiPilotos, EditaPilotos
# from pilotos.views import Login, CriaUsuario
from pilotos.views import PilotosList
# from pilotos.views import PilotosView


urlpatterns = [
    path('', Home.as_view(), name='Pilotos-home'),
    
    # path('pilotos/', PilotosView.as_view(), name="piloto-view"),
    path('pilotos/', PilotosList.as_view(), name="piloto-list"),

    path('pilotos/<int:pk>/', PilotosDetail.as_view(), name='piloto-detail'),

    path('pilotos/criar/', AdicionaPilotos.as_view()),
    path('pilotos/<int:pk>/deletar/', ExcluiPilotos.as_view(), name='piloto-deletar'),
    path('pilotos/<int:pk>/editar/', EditaPilotos.as_view(), name='piloto-editar'),
    
    # path('criar_usuario/', CriaUsuario.as_view()),
    # path('login/', Login.as_view()),

    ]
