from django.db import models

class Receta(models.Model):
    title = models.CharField(verbose_name="Título", max_length=50)
    subtitle = models.CharField(verbose_name="Subtitulo", max_length=100, null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="recetas")
    ingredients = models.TextField(verbose_name="Ingredientes")
    preparation = models.TextField(verbose_name="Preparacíon")  
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Edición")

    class Meta:
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ['created']

    def __str__(self):
        return self.title


class Comentario(models.Model):

   #AVERIGUAR COMO PASARLE EL ID DE LA RECETA AL COMENTARIO

    message = models.CharField(verbose_name="Mensaje", max_length=300)
    likes = models.IntegerField(verbose_name="Likes", default=0)
    receta_id = models.ForeignKey(Receta, on_delete=models.CASCADE, null=False, blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha Edición")

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        ordering = ['created']

    def __str__(self):
        return self.message