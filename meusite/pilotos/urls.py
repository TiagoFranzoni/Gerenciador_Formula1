"""docstring"""
from django.urls import path
from pilotos.views import PilotosView, PilotosViewDetail, PilotosViewExclui, PilotosViewEdita, PilotosViewAdiciona
from pilotos.views import PilotosList, PilotosDetailList
# from pilotos.views import PilotosView


urlpatterns = [   
    path('view/pilotos/', PilotosView.as_view(), name="piloto-view"),
    path('view/pilotos/detail/<int:pk>/', PilotosViewDetail.as_view(), name='piloto-view-detail'),
    path('view/pilotos/criar/', PilotosViewAdiciona.as_view(), name='piloto-view-criar'),
    path('view/pilotos/<int:pk>/deletar/', PilotosViewExclui.as_view(), name='piloto-deletar'),
    path('view/pilotos/<int:pk>/editar/', PilotosViewEdita.as_view(), name='piloto-editar'),

    path('pilotos/', PilotosList.as_view(), name="piloto-list"),
    path('pilotos/<int:pk>/', PilotosDetailList.as_view(), name='piloto-detail'),
    path('pilotos/criar/', PilotosDetailList.as_view(), name='piloto-api-criar'),
    ]
