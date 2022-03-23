from email import message
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import content_form, registerForm
from django.contrib import messages
from .models import content
from django.contrib.auth.models import User

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request,'Login/login.html')
    def post(self,request):
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request,username = username,password = password)
        if user is None:
            messages.success(request, ("Username or password not exactly. Please try again..."))
            return render(request,'Login/login.html')
        else:
            login(request, user)
            return render(request,'Login/index.html')

class index(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
       ct = content_form
       context = {'ctf': ct}
       return render(request,'Login/index.html',context)
    def post(self,request):
        ct = content_form(request.POST)
        if ct.is_valid():
            ct.save()
        else:
            return HttpResponse("Lưu không thành công")
        return HttpResponse("Lưu thành công")
def Logout(request):
    logout(request)
    return redirect('Login:Login')

class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request,'Login/register.html', {'rF': rF})
    def post(self, request):
        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        user = User.objects.create_user(uname,email, pwd)
        user.last_name = 'Ho'
        user.first_name = 'Ngoc'
        messages.success(request, ("Register successfully. Please login..."))
        user.save()
        return redirect('Login:Login')
