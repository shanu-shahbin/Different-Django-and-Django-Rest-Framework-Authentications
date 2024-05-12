
from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.custom_login, name='login'),
    path('success/', views.success_view, name='success_url'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),   
]


    
   
  # 
