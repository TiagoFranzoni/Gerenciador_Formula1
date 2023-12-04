"""docstring"""
from django.urls import path
from carros.views import CarrosView, CarrosViewDetail, CarrosViewExclui, CarrosViewEdita, CarrosViewAdiciona
from carros.views import CarrosList, CarrosDetailList
# from carros.views import CarrosView


urlpatterns = [
    path('view/carros/', CarrosView.as_view(), name="carro-view"),
    path('view/carros/detail/<int:pk>/', CarrosViewDetail.as_view(), name='carro-view-detail'),
    path('view/carros/criar/', CarrosViewAdiciona.as_view(), name='carro-view-criar'),
    path('view/carros/<int:pk>/deletar/', CarrosViewExclui.as_view(), name='carro-deletar'),
    path('view/carros/<int:pk>/editar/', CarrosViewEdita.as_view(), name='carro-editar'),

    path('carros/', CarrosList.as_view(), name="carro-list"),
    path('carros/<int:pk>/', CarrosDetailList.as_view(), name='carro-detail'),
    path('carros/criar/', CarrosDetailList.as_view(), name='carro-api-criar'),
    ]
