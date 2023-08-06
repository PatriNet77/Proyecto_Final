from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/detail', PostDetailView.as_view(), name='post_individual'), 
    path("posts/", PostCreateView.as_view(), name="post_crear"),
    path("posts/<int:pk>/modificar/", PostUpdateView.as_view(), name="post_modificar"),
    path("posts/<int:pk>/eliminar/", PostDeleteView.as_view(), name="post_eliminar"),
    path("posts/categoria", CategoriaCreateView.as_view(), name="categoria_crear"),
    path("categoria", CategoriaListView.as_view(), name="categoria_lista"),
    path("categoria/<int:pk>/posts/", PostPorCategoriaView.as_view(), name="post_por_categoria"),
    path("categoria/<int:pk>/delete/", CategoriaDeleteView.as_view(), name="categoria_eliminar"),
    path("comentario/<int:pk>/editar/", ComentarioUpdateView.as_view(), name="comentario_modificar"),
    path("comentario/<int:pk>/eliminar/", ComentarioDeleteView.as_view(), name="comentario_eliminar"),
]
