from django.urls import path, include
from .views import *

app_name = 'danhmuc'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('danhmuc/', QuanLyDanhMucView.as_view(), name='qldanhmuc')
]
