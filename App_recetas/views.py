from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import View
from .forms import ComentarioForm
from .models import Receta, Comentario

from django.http import JsonResponse
#-----------------------------------------------------------------------

class RecetaListView(ListView):

    model = Receta
    template_name = "App_recetas/main_recetas.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(RecetaListView, self).dispatch(request, *args, **kwargs)


#-----------------------------------------------------------------------

class BuscarRecetasListView(TemplateView):

    template_name = "App_recetas/buscar_Recetas.html"
    recetas = Receta.objects.all()

    def get_context_data(self, *args, **kwargs):
        
        context = ({
            'title':'Buscar receta',
            'recetas':self.recetas
        })

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(BuscarRecetasListView, self).dispatch(request, *args, **kwargs)

#-----------------------------------------------------------------------#

class RecetaDetailView(DetailView):

    model = Receta

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(RecetaDetailView, self).dispatch(request, *args, **kwargs)
        
#-----------------------------------------------------------------------#

class RecetaCreate(CreateView):
    model = Receta
    template_name = "App_recetas/crear_receta.html"
    fields = ['title', 'subtitle', 'image', 'ingredients', 'preparation']
    success_url = reverse_lazy('recetas')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(RecetaCreate, self).dispatch(request, *args, **kwargs)

#-----------------------------------------------------------------------#

class ComentariosRecetaListView(ListView):

    model = Comentario
    template_name = "App_recetas/comentarios.html"

    #recoger la variable para filtrar según su valor
    def get_queryset(self):
        #obtengo el parametro 
        parametro = self.kwargs['id_receta']
        #filtro mi modelo según el parametro
        query = super().get_queryset()
        comentarios = Comentario.objects.filter(receta_id=parametro) 

        return comentarios

    def get_context_data(self, **kwargs):
        some_context = self.kwargs['id_receta']
        context = super(ComentariosRecetaListView, self).get_context_data(**kwargs)
        context['context'] = some_context

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(ComentariosRecetaListView, self).dispatch(request, *args, **kwargs)

#-----------------------------------------------------------------------#

class ComentarioCreate(CreateView):

    model = Comentario
    form_class = ComentarioForm
    template_name = "App_recetas/crear_comentario.html"
    success_url = reverse_lazy('recetas')

    def get_context_data(self, **kwargs):
        some_context = self.kwargs['id_receta']
        context = super(ComentarioCreate, self).get_context_data(**kwargs)
        context['context'] = some_context

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(ComentarioCreate, self).dispatch(request, *args, **kwargs)

#-----------------------------------------------------------------------#


#AVERIGUAR COMO ELIMINAR UNA RECETA

