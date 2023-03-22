
from telnetlib import LOGOUT
from django.shortcuts import render,HttpResponse, redirect
from app.models import Contact,Decoration,Book_Deco,Babysitter
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random,smtplib
from django.core.mail import send_mail
from django.db import models

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def service(request):
    return render(request, 'service.html')

def payment(request):
    return render(request, 'payment.html')


def decoration(request):
     if request.method == "POST":
        decofor = request.POST.get('decofor')
        flat = request.POST.get('flat')
        cleaning = request.POST.get('cleaning')
        materials = request.POST.get('materials')
        decoration = Decoration(decofor=decofor,flat=flat,cleaning=cleaning,materials=materials)
        decoration.Customer_Name= request.user
        decoration.save()
        messages.success(request, 'Thankyou for filling the form,Please proceed with booking')
        return redirect('/bookideco')
     return render(request, 'decoration.html')

def bookideco(request):
    if request.method == "POST":
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        bookideco= Book_Deco(address=address, city=city, pincode=pincode)
        bookideco.Cust_Name = request.user
        bookideco.save()
        return redirect("https://rzp.io/l/RLyFJKRW1M")
    return render(request, 'bookideco.html')

def babysitter(request):
     if request.method == "POST":
        age= request.POST.get('age')
        gender= request.POST.get('gender')
        babymess= request.POST.get('babymess')
        
        baby = Babysitter(age=age, gender=gender,babymess=babymess)
        baby.Customer_Name= request.user
        baby.save()
        return redirect('/bookint')
     return render(request, 'babysitter.html')

def bookint(request,email=None):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('we.are.happy.helpers@gmail.com','fafmnvrhwxuauodm')
    msg='Hello,' + '\nWe are Happy Helpers' + '\nYour google meet link - https://meet.google.com/niy-bffu-emv ' + '\nGet to know your babysitter' + '\nThank you.'
    msg1='Hello Happy Helper' + '\nYou have been assigned as Babysitter.' + '\nInterview with the customer has been scheduled in 5 mins' +  '\nGoogle meet link - https://meet.google.com/niy-bffu-emv' + '\nThank you.'
    server.sendmail('we.are.happy.helpers@gmail.com','mayyerande@gmail.com',msg)
    server.sendmail('we.are.happy.helpers@gmail.com','2020.kedar.gawhankar@ves.ac.in',msg1)
    server.quit()
    
    return render(request, 'bookint.html')

def bookbaby(request):
    return render(request, 'bookbaby.html')

def acceptbaby(request,email=None):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('we.are.happy.helpers@gmail.com','fafmnvrhwxuauodm')
    msg='Hello Happy Helper,' + '\nYou have been accepted by the customer as babysitter.' + '\nCustomer Name: Mayuri Yerande' + '\nVerification Code will soon be sent' + '\nThank you.'
    server.sendmail('we.are.happy.helpers@gmail.com','2020.kedar.gawhankar@ves.ac.in',msg)
    server.quit()
    
    return render(request,'acceptbaby.html')

def reject(request):
    return render(request,'reject.html')

def verify(request,email=None):
    otp=''.join([str(random.randint(0,9)) for i in range(4)])
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('we.are.happy.helpers@gmail.com','fafmnvrhwxuauodm')
    msg='Hello,' + '\nWe are Happy Helpers' + '\nYour verification code is ' + str(otp) + '\nPlease Verify this code with your helper.' + '\nThank you.'
    msg1='Hello Happy Helper' + 'You have been assigned as Babysitter' + '\nYour verification code is ' + str(otp) + '\nPlease Verify this code with the customer.' + '\nThank you.'
    server.sendmail('we.are.happy.helpers@gmail.com','mayyerande@gmail.com',msg)
    server.sendmail('we.are.happy.helpers@gmail.com','2020.kedar.gawhankar@ves.ac.in',msg1)
    server.quit()

    return render(request,'verify.html')

def verfication(request,email=None):
    # if request.method == "POST":
    #     usernames = request.POST.get('usernames')
    #     email = request.POST.get('email')
    #     pass1 = request.POST.get('pass1')
    #     myuser = User.objects.create_user(usernames,email,pass1)
    
    otp=''.join([str(random.randint(0,9)) for i in range(4)])
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('we.are.happy.helpers@gmail.com','fafmnvrhwxuauodm')
    msg='Hello,' + '\nWe are Happy Helpers' + '\nYour verification code is ' + str(otp) + '\nPlease Verify this code with your helper.' + '\nThank you.'
    msg1='Hello,' + '\nWe are Happy Helpers' + 'You have been assigned "Decoration for Christmas" service' + '\nYour verification code is ' + str(otp) + '\nPlease Verify this code with the customer.' + '\nThank you.'
    server.sendmail('we.are.happy.helpers@gmail.com','mayyerande@gmail.com',msg)
    server.sendmail('we.are.happy.helpers@gmail.com','2020.kedar.gawhankar@ves.ac.in',msg1)
    server.quit()
    
    return render(request, 'verfication.html')
    

def cleaning(request):
    return render(request, 'cleaning.html')

def success(request):
    return render(request, 'success.html')


def layout(request):
    return render(request, 'layout.html')

def signuphelper(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     phone = request.POST.get('phone')
    #     pass12 = request.POST.get('pass12')
    #     pass13 = request.POST.get('pass13')

    return render(request, 'signuphelper.html')

def loginhelper(request):
    return render(request, 'loginhelper.html')

def logouthelper(request):
    logout(request)
    return render(request, 'index.html')

def helperhome(request):
    return render(request, 'helperhome.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def cooking(request):
    return render(request, 'cooking.html')

def caretaker(request):
    return render(request, 'caretaker.html')

def loginuser(request):
    if request.method == 'POST':
        usernames = request.POST.get('usernames')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username =usernames ,password=pass1)
        if user is not None:
            login(request, user)
            fname= user.first_name
            return render(request, 'home.html', {'fname':fname})
        else:
            messages.error(request,"Please enter correct username or password, Try again")
            return redirect("/login")
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return render(request, 'index.html')
    

def signup(request):
    if request.method == "POST":
        usernames = request.POST.get('usernames')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(usernames,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
       
        myuser.save
        messages.success(request,"your account has been created succesfully")
        return redirect("/login")
    return render(request, 'signup.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent successfully. Thank you')
    return render(request, 'contact.html')