from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/user-default.png')
#    es_colaborador = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('index')
    
@receiver(post_save, sender=AbstractUser)
def crear_actualizar_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)
    else:
        try:
            instance.usuario.save()
        except Usuario.DoesNotExist:
            pass
        
class Profile(models.Model):
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
            
    def __str__(self):
        return self.usuario.username

class Colaborador(models.Model):
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nombre

