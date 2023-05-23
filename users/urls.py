from django.urls import path, include, re_path
from . import views
from .views import CustomLogoutView

app_name = 'users'
urlpatterns = [
    # Dolaczenie domyslnych adresow uwierzytelnienia
    path('', include('django.contrib.auth.urls')),
    # Strona rejestracji
    re_path('register/', views.register, name='register'),
    path('user_logout/', CustomLogoutView.as_view(), name='user_logout'),
 
]
