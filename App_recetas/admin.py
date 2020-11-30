from django.contrib import admin
from .models import Receta, Comentario

# Register your models here.

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'title', 'subtitle', 'ingredients', 'preparation')

class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'message', 'likes', 'receta_id')

admin.site.register(Receta, RecetaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
