"""docstring"""
from django.urls import path
from equipes.views import Home
from equipes.views import EquipesView, EquipesViewDetail, EquipesViewExclui, EquipesViewEdita, EquipesViewAdiciona
from equipes.views import EquipesList, EquipesDetailList
from equipes.views import Login, CriaUsuario


urlpatterns = [
    path('', Home.as_view(), name='equipes-home'),

    path('view/equipes/', EquipesView.as_view(), name="equipe-view"),
    path('view/equipes/detail/<int:pk>/', EquipesViewDetail.as_view(), name='equipe-view-detail'),
    path('view/equipes/criar/', EquipesViewAdiciona.as_view(), name='equipe-view-criar'),
    path('view/equipes/<int:pk>/deletar/', EquipesViewExclui.as_view(), name='equipe-deletar'),
    path('view/equipes/<int:pk>/editar/', EquipesViewEdita.as_view(), name='equipe-editar'),

    path('equipes/', EquipesList.as_view(), name="equipe-list"),
    path('equipes/<int:pk>/', EquipesDetailList.as_view(), name='equipe-detail'),
    path('equipes/criar/', EquipesDetailList.as_view(), name='equipe-api-criar'),

    path('criar_usuario/', CriaUsuario.as_view()),
    path('login/', Login.as_view()),
    ]
