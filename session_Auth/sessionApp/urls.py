from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),  # Corrected this line
]
