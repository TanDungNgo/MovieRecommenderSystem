from django.urls import path, include
from . import views  # Thay thế bằng tên module và view của bạn

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('admin/', include('admin_page.urls')),
    path('profile/', views.profile, name='profile'),
]
