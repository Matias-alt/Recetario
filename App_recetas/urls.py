from django.urls import path
from .views import RecetaListView, RecetaCreate, RecetaDetailView, ComentariosRecetaListView, ComentarioCreate, BuscarRecetasListView

urlpatterns = [
    path('recetas/', RecetaListView.as_view(), name="recetas"),
    path('receta/<int:pk>/', RecetaDetailView.as_view(), name="receta"),
    path('buscar_recetas/', BuscarRecetasListView.as_view(), name="buscar_recetas"),
    path('crear_receta/', RecetaCreate.as_view(), name="crear_receta"),
    path('comentarios/<int:id_receta>/', ComentariosRecetaListView.as_view(), name="comentarios"),
    path('crear_comentario/<int:id_receta>/', ComentarioCreate.as_view(), name="crear_comentario"),
]