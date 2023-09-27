from django.urls import path
from . import views

urlpatterns = [
    #User
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail', views.blog_detail, name='blog_detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    #Admin
    path('general/', views.general, name='general'),
    path('general/blank/', views.blank, name='blank'),
    path('general/button/', views.button, name='button'),
    path('general/chart/', views.chart, name='chart'),
    path('general/element/', views.element, name='element'),
    path('general/form/', views.form, name='form'),
    path('general/table/', views.table, name='table'),
    path('general/typography/', views.typography, name='typography'),
    path('general/widget/', views.widget, name='widget'),
    path('general/signin/', views.signin, name='signin'),
    path('general/signup/', views.signup, name='signup'),
]
