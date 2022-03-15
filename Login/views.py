from email import message
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import content_form
from django.contrib import messages
from .models import content

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request,'Login/login.html')
    def post(self,request):
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(request,username = username,password = password)
        if user is None:
            messages.success(request, "Errorr." )
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
