from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate, login

class RegistroUsuarioForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'imagen']
        
    def clean_email(self):
        email_field = self.cleaned_data['email']
        
        if Usuario.objects.filter(email=email_field).exist():
            raise forms.ValidationError('Este correo ya está registrado')
        
        return email_field
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

