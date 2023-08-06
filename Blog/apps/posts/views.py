from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.db.models.functions import Lower
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria, Comentario
from .forms import ComentarioForm, CrearPostForm, NuevaCategoriaForm

#404
class NotFoundView(TemplateView):
    template_name = '404.html'

#Post lista, individual, crear, modificar, eliminar
#y consulta a la base de datos
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        orden = self.request.GET.get('orden')
        if orden == 'Reciente':
            queryset = queryset.order_by('-fecha')
        elif orden== 'Mas antiguo':
            queryset = queryset.order_by('fecha')
        elif orden == 'Alfabetico A-Z':
            queryset = queryset.annotate(titulo_lower=Lower('titulo')).order_by('titulo_lower')
        elif orden == 'Alfabetico Z-A':
            queryset = queryset.annotate(titulo_lower=Lower('titulo')).order_by('-titulo_lower')

        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria_id=categoria)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orden'] = self.request.GET.get('orden', 'reciente')
        context['categorias'] = Categoria.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'post_individual'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(post_id=self.kwargs['id'])
        return context
    
    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.usuario
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model= Post
    form_class = CrearPostForm
    template_name = 'posts/post_crear.html'
    success_url = reverse_lazy('apps.posts:posts')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CrearPostForm
    template_name = 'posts/post_modificar.html'
    success_url = reverse_lazy('apps.posts:posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_eliminar.html'
    success_url = reverse_lazy('apps.posts:posts')

class PostPorCategoriaView(ListView):
    model = Post
    template_name = 'posts/post_por_categoria.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(categoria_id=self.kwargs['pk'])

#Categoría crear, listar, eliminar
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model= Categoria
    form_class = NuevaCategoriaForm
    template_name = 'posts/categoria_crear.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('apps.posts:post_crear')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'posts/categoria_lista.html'
    context_object_name = 'categoria'

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'posts/categoria_eliminar.html'
    success_url = reverse_lazy('apps.posts:categoria_lista')

#Comentario crear, modificar, eliminar
class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/comentario_agregar.html'
    success_url = 'comentario/comentarios/'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.post_id = self.kwargs['posts_id']
        return super().form_valid(form)

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentario/comentario_modificar.html'
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse('apps.posts:post_individual', args=[self.object.posts.id])

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comentario/comentario_eliminar.html'
    def get_success_url(self):
        return reverse('apps.posts:post_individual', args=[self.object.posts.id])
