from .models import Usuario 
from apps.posts.models import Post, Comentario
from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

# Create your views here.

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'registration/registrar.html' 
        
    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión')
        group = Group.objects.get(name='Registrado')
        self.object.groups.add(group)
        return redirect('apps.usuario:registrar')
    
class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Ya era hora! Dónde andabas?.')
        
        return reverse('index')
    
class LogoutUsuario(LogoutView):
    template_name = 'registration/logout.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Te fuiste, traidor!')
        
        return reverse('index')

class UsuarioListView(LoginRequiredMixin, ListView):
    model= Usuario
    template_name = 'usuario/usuario_lista.html'

    def get_queryset(self):
        queryset = super().queryset()
        queryset = queryset.exclude(is_superuser=True)
        return queryset

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model= Usuario
    template_name = 'usuario/usuario_eliminar.html'
    success_url = reverse_lazy('apps.usuario:usuario_lista')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        colaborador_group = Group.objects.get(name='Colaborador')
        es_colaborador = colaborador_group in self.object.groups.all()
        context["es_colaborador"] = es_colaborador
        return context
    
    def post(self, request, *args, **kwargs):
        eliminar_comentarios = request.POST.get('eliminar_comentarios', False)
        eliminar_posts = request.POST.get('eliminar_posts', False)
        self.object = self.get_object()
        if eliminar_comentarios:
            Comentario.objects.filter(usuario=self.object).delete()
        
        if eliminar_posts:
            Post.objects.filter(autor=self.object).delete()
        messages.success(request, f'Usuario {self.object.username} eliminado correctamente')
        return self.delete(request, *args, **kwargs)
    
        
        