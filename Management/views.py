from Management.models import UserDetail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def Home(request):
    d = {'title':'Fashion Hub'}
    return render(request, 'index.html', d)

def Contact(request):
    d = {'title':'Contact - FashionHub'}
    return render(request, 'contact.html', d)

def About(request):
    d = {'title':'About - FashionHub'}
    return render(request, 'about.html', d)

def Login(request):
    if 'Login' in request.POST:
        print("inside Login")
        un = request.POST['Name']
        pwd = request.POST['Password'] 
        auth = authenticate(username=un, password = pwd)
        if auth:
            login(request, auth)
        else:
            return HttpResponse("Error")
    return redirect('home')

def Logout(request):
    logout(request)
    return redirect('home')

def Register(request):
    if "Register" in request.POST:
        fn = request.POST["Name"]
        un = request.POST["Username"]
        e = request.POST["Email"]
        m = request.POST["mobile"]
        pwd1 = request.POST["Password1"]
        pwd2 = request.POST["Password2"]
        check = User.objects.filter(username=un).first()
        if pwd1 != pwd2:
            return HttpResponse("Password does not match")
        elif check:
            return HttpResponse("Username Already Taken")
        else:
            User.objects.create_user(username=un, email = e, password = pwd1, first_name = fn)
            auth = authenticate(username=un, password=pwd1)
            login(request, auth)
            UserDetail.objects.create(user = request.user, mob = m)
    return redirect('home')