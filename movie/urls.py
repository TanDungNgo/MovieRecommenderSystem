from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail', views.blog_detail, name='blog_detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]