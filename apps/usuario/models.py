from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/user-default.png')

    def get_absolute_url(self):
        return reverse('{% load index_tags %}')
