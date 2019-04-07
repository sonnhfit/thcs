from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/')
        return self.get(request)
