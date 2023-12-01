"""docstring"""
from django.urls import path
from equipes.views import EquipesDetail, Home, AdicionaEquipes, ExcluiEquipes, EditaEquipes
from equipes.views import Login, CriaUsuario
from equipes.views import EquipesList
# from Equipes.views import EquipesView


urlpatterns = [
    path('', Home.as_view(), name='equipes-home'),
    
    # path('equipes/', EquipesView.as_view(), name="equipe-view"),
    path('equipes/', EquipesList.as_view(), name="equipe-list"),

    path('equipes/<int:pk>/', EquipesDetail.as_view(), name='equipe-detail'),

    path('equipes/criar/', AdicionaEquipes.as_view()),
    path('equipes/<int:pk>/deletar/', ExcluiEquipes.as_view(), name='equipe-deletar'),
    path('equipes/<int:pk>/editar/', EditaEquipes.as_view(), name='equipe-editar'),
    
    path('criar_usuario/', CriaUsuario.as_view()),
    path('login/', Login.as_view()),

    ]
