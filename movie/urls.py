from django.urls import path
from . import views

urlpatterns = [
    #User
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_detai/', views.blog_detail, name='blog_detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('search_page/', views.search_page, name='search_page'),
    path('movie_detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    
]
