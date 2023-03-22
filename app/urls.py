
from django.contrib import admin
from django.urls import path
from app import views
# from .views import bookideco
urlpatterns = [
    path("",views.index, name='home'),
    path("home",views.home, name='home'),
    path("service", views.service ,name='service'),
    path("decoration",views.decoration , name='decoration'),
    path("babysitter",views.babysitter , name='babysitter'),
    path("cleaning",views.cleaning , name='cleaning'),
    path("cooking",views.cooking , name='cooking'),
    path("caretaker",views.caretaker , name='caretaker'),
    path("login",views.loginuser , name='login'),
    path("logout",views.logoutuser , name='logout'),
    path("signup",views.signup , name='signup'),
    path("contact",views.contact , name='contact'),
    path("about",views.about, name='about'),
    path("bookideco",views.bookideco, name='bookideco'),
    path("signuphelper",views.signuphelper, name='signuphelper'),
    path("loginhelper",views.loginhelper, name='loginhelper'),
    path("logouthelper",views.logouthelper, name='logouthelper'),
    path("helperhome",views.helperhome, name='helperhome'),
    path("payment",views.payment, name='payment'),
    path("verfication",views.verfication, name='verfication'),
    path("success",views.success, name='success'),
    path("bookbaby",views.bookbaby, name='bookbaby'),
    path("bookint",views.bookint, name='bookint'),
    path("acceptbaby",views.acceptbaby, name='acceptbaby'),
    path("reject",views.reject, name='reject'),
    path("verify",views.verify, name='verify'),
    path("profile",views.profile, name='profile'),
    path("layout",views.layout, name='layout'),



]
