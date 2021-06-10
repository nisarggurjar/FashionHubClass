from Management.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def commonData():
    category = Category.objects.all()
    subCategory = SubCategory.objects.all()
    return {'category':category, 'subCategory':subCategory}

def Home(request):
    d = {'title':'Fashion Hub'}
    products = Product.objects.all()
    d.update({'products':products})
    if request.session.has_key('userError'):
        d.update({'userError':True})
        del request.session['userError']

    if request.session.has_key('errorPWD'):
        d.update({'errorPWD':True})
        del request.session['errorPWD']

    if request.session.has_key('errorUsername'):
        d.update({'errorUsername':True})
        del request.session['errorUsername']

    d.update(commonData())
    return render(request, 'index.html', d)

def Contact(request):
    d = {'title':'Contact - FashionHub'}
    if request.session.has_key('userError'):
        d.update({'userError':True})
        del request.session['userError']

    if request.session.has_key('errorPWD'):
        d.update({'errorPWD':True})
        del request.session['errorPWD']

    if request.session.has_key('errorUsername'):
        d.update({'errorPWD':True})
        del request.session['errorUsername']

    d.update(commonData())

    if 'contactForm' in request.POST:
        n = request.POST['name']
        e = request.POST['email']
        msg = request.POST['msg']
        ContactForm.objects.create(name = n, email = e, message = msg)
    return render(request, 'contact.html', d)

def About(request):
    d = {'title':'About - FashionHub'}
    if request.session.has_key('userError'):
        d.update({'userError':True})
        del request.session['userError']

    if request.session.has_key('errorPWD'):
        d.update({'errorPWD':True})
        del request.session['errorPWD']

    if request.session.has_key('errorUsername'):
        d.update({'errorPWD':True})
        del request.session['errorPWD']
    
    d.update(commonData())
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
            request.session['userError'] = True
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
            request.session['errorPWD'] = True
        elif check:
            request.session['errorUsername'] = True
        else:
            User.objects.create_user(username=un, email = e, password = pwd1, first_name = fn)
            auth = authenticate(username=un, password=pwd1)
            login(request, auth)
            UserDetail.objects.create(user = request.user, mob = m)
    return redirect('home')