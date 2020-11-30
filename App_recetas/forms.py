from django.forms import *
from .models import Comentario 

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['message', 'receta_id']

        widgets = {
            'message':Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un comentario',
                    'autocomplete': 'off',
                    'rows': '3',
                }
            ),

            'receta_id':Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }