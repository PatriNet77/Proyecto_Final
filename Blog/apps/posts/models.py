from django.db import models
from django.utils import timezone
from django.conf import settings
import os

#Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.nombre

#Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/ia_top.jpg')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)
    
    def __str__(self):
        return self.titulo
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Post, self).delete(*args, **kwargs)
        
    @property
    def total_comentarios(self):
        return self.comentarios.count()

#Comentario
class Comentario(models.Model):
    posts = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.texto