# Generated by Django 3.1 on 2020-09-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_recetas', '0005_auto_20200916_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='image',
            field=models.ImageField(default=0, upload_to='recetas', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]
