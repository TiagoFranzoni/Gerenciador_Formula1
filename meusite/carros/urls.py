"""docstring"""
from django.urls import path
from carros.views import CarrosDetail, AdicionaCarros, ExcluiCarros, EditaCarros, CarrosView
from carros.views import CarrosList
# from carros.views import EquipesView


urlpatterns = [
    path('list/', CarrosView.as_view(), name="carro-view"),
    path('', CarrosList.as_view(), name='carro-list'),

    path('<int:pk>/', CarrosDetail.as_view(), name='carro-detail'),

    path('criar/', AdicionaCarros.as_view()),
    path('<int:pk>/deletar/', ExcluiCarros.as_view(), name='carro-deletar'),
    path('<int:pk>/editar/', EditaCarros.as_view(), name='carro-editar'),

]