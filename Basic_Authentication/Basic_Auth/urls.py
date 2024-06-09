from django.urls import path
from .views import user_api_view

urlpatterns = [
    path('user/', user_api_view),
]

