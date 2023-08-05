from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/detail', views.PostDetailView.as_view(), name='posteo'), 
    path("posts/", views.PostCreateView.as_view(), name="post_crear"),
    path("posts/<int:pk>/modificar/", views.PostUpdateView.as_view(), name="post_modificar"),
    path("posts/<int:pk>/eliminar/", views.PostDeleteView.as_view(), name="post_eliminar"),
    path("posts/categoria", views.CategoriaCreateView.as_view(), name="categoria_crear"),
    path("categoria", views.CategoriaListView.as_view(), name="categoria_lista"),
    path("categoria/<int:pk>/delete/", views.CategoriaDeleteView.as_view(), name="categoria_eliminar"),
    path("comentario/<int:pk>/editar/", views.ComentarioUpdateView.as_view(), name="comentario_modificar"),
    path("comentario/<int:pk>/eliminar/", views.ComentarioDeleteView.as_view(), name="comentario_eliminar"),

]
