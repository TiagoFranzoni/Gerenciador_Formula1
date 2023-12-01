"""docstring"""
from django.urls import path
from carros.views import CarrosDetail, Home, AdicionaCarros, ExcluiCarros, EditaCarros
from carros.views import CarrosList
# from carros.views import EquipesView


urlpatterns = [
    # path('', Home.as_view(), name='carros-home'),
    path('carros/', Home.as_view(), name='carros-home'),

    # path('carros/', EquipesView.as_view(), name="carro-view"),
    # path('carros/', CarrosList.as_view(), name='carro-list'),

    path('carros/<int:pk>/', CarrosDetail.as_view(), name='carro-detail'),

    path('carros/criar/', AdicionaCarros.as_view()),
    path('carros/<int:pk>/deletar/', ExcluiCarros.as_view(), name='carro-deletar'),
    path('carros/<int:pk>/editar/', EditaCarros.as_view(), name='carro-editar'),

    ]