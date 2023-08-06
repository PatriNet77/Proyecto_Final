from django.shortcuts import render
from apps.posts.models import Post
from django.http import HttpResponseNotFound

def index(request):
    post_recientes = Post.objects.all().order_by('-fecha')[0:5]
    contexto = {
        'post_recientes':post_recientes
        }
    return render(request, 'index.html', contexto)

def pagina_404(request, exception):
    return HttpResponseNotFound('404.html')