from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class RegistrarUsuario(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registration/registrar.html' 
        
    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión')
        form.save()
        
        return redirect('apps.usuario:login')
    
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
    
#class ProfileViews(CustomTemplateView):
#    template_name = 'usuario/profile.html'