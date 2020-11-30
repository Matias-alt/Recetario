from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy



class RegistroPageView(TemplateView):
    template_name = "App_registro/registro.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Registro'})

class LoginPageView(TemplateView):
    template_name = "App_registro/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Login'})

  
