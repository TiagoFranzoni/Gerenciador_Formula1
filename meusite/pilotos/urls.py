"""docstring"""
from django.urls import path
from pilotos.views import PilotosDetail, AdicionaPilotos, ExcluiPilotos, EditaPilotos
from pilotos.views import PilotosList
# from pilotos.views import PilotosView


urlpatterns = [   
    # path('', PilotosView.as_view(), name="piloto-view"),
    path('', PilotosList.as_view(), name="piloto-list"),

    path('<int:pk>/', PilotosDetail.as_view(), name='piloto-detail'),

    path('criar/', AdicionaPilotos.as_view()),
    path('<int:pk>/deletar/', ExcluiPilotos.as_view(), name='piloto-deletar'),
    path('<int:pk>/editar/', EditaPilotos.as_view(), name='piloto-editar'),

    ]
