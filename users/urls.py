from django.urls import path, include
from .views import *
app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
