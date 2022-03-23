from django.urls import path
from . import views

app_name = 'Login'

urlpatterns = [
    path('login/',views.Login.as_view(), name='Login'),
    path('',views.index.as_view(), name='index'),
    path('logout/',views.Logout, name='Logout'),
    path('register/',views.registerUser.as_view(), name='Register')
]
