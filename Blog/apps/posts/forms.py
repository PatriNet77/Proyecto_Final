from django import forms
from .models import Comentario, Post, Categoria

class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","subtitulo","texto","activo","categoria","imagen"]

class NuevaCategoriaForm(forms.ModelForm):
    class Meta: 
        model= Categoria
        fields = "__all__"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields =["usuario", "texto"]