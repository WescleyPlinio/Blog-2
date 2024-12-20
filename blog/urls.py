from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('criar_post/', views.criar_post, name='criar_post'),
    path('mensagens/', views.mensagens, name='mensagens'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar_mensagem/<int:mensagem_id>/editar/', 
         views.editar_mensagem, name='editar_mensagem'),
    path('deletar_mensagem/<int:mensagem_id>/deletar/', 
         views.deletar_mensagem, name='deletar_mensagem'),
    path('editar_post/<int:post_id>/editar/', 
         views.editar_post, name='editar_post'),
    path('deletar_post/<int:post_id>/deletar/', 
         views.deletar_post, name='deletar_post'),
]
