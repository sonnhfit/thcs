from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
# Create your views here.


class IndexView(LoginRequiredMixin, View):
    login_url = 'user/login/'

    def get(self, request):
        return render(request, 'index.html')


class QuanLyDanhMucView(LoginRequiredMixin, View):
    login_url = 'user/login/'

    def get(self, request):
        return render(request, 'danhmuc.html')
