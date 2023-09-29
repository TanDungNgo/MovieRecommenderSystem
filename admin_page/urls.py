from django.urls import path
from . import views

urlpatterns = [
    path('', views.general, name='general'),
    path('button/', views.button, name='button'),
    path('chart/', views.chart, name='chart'),
    path('element/', views.element, name='element'),
    path('table/', views.table, name='table'),
]
