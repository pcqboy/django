from django.db import models

# Create your models here.
class livro(models.Model):
    titulo = models.CharField(max_length=40, verbose_name="Título")
    autor = models.CharField(max_length=20, verbose_name="Autor")