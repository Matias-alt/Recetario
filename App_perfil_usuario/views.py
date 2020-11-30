from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from App_recetas.models import Receta

class PerfilPageView(TemplateView):
    template_name = "App_perfil_usuario/perfil.html"
    recetas = Receta.objects.all()

    def get_context_data(self, *args, **kwargs):
        
        context = ({
            'title':'Perfil',
            'recetas':self.recetas
        })

        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))

        return super(PerfilPageView, self).dispatch(request, *args, **kwargs)
                                                    
