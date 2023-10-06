from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('table/', views.table, name='table'),
    path('create/', views.create_movie, name='create_movie'),
    path('list/', views.movie_list, name='movie_list'),
]
