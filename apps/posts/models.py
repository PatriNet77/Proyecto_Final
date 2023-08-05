import os
from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils import timezone

#Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.nombre

#Post Admin
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'activo', 'categoria')
    list_filter = ('activo', 'categoria')
    actions=['publicar', 'ocultar']
    
    def publicar(self, request, queryset):
        queryset.update(activo=True)

    def ocultar(self, request, queryset):
        queryset.update(activo=False)

#Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    imagen = models.ImageField(null=True, blank=True, upload_to='media/posts', default='static/img/post_default.jpg')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)
    
    def __str__(self):
        return self.titulo
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
            super(Post, self).delete(*args, **kwargs)
        
#Comentario
class Comentario(models.Model):
    posts = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    comentario_aprobado = models.BooleanField(default=False)
    
    def aprobado(self):
        self.comentario_aprobado = True
        self.save()
        
    def __str__(self):
        return self.texto