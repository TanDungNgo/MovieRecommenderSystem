from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('create/', views.create_movie, name='create_movie'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('user_list/', views.user_list, name='user_list'),
    path('export_movies/', views.export_movies, name='export_movies'),
    path('export_users/', views.export_users, name='export_users'),
]
