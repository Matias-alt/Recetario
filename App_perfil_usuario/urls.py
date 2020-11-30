from django.urls import path
from .views import PerfilPageView
from App_recetas.views import RecetaCreate

urlpatterns = [
    path('perfil/', PerfilPageView.as_view(), name="perfil"),
    path('nueva_receta/', RecetaCreate.as_view(), name="nueva_receta"),
]