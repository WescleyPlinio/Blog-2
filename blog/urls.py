from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('mensagens/', views.mensagens, name='mensagens'),
]
