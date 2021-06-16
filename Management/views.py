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
        un = request.POST['Name']
        pwd = request.POST['Password'] 
        auth = authenticate(username=un, password = pwd)
        if auth:
            login(request, auth)
            if request.user.is_staff:
                return redirect('adminPanel')
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



def AdminPanel(request):
    if not request.user.is_staff:
        return redirect('home')
    
    return render(request, 'index2.html', {"title": "Admin Panel"})


def ManageCategory(request):
    d = {'title':'Manage Category'}
    categories = Category.objects.all()
    d.update({"categories":categories})
    if 'addCat' in request.POST:
        t = request.POST['cat']
        Category.objects.create(title = t)
    return render(request, 'manageCateory.html',d)

def DeleteCategory(request, cid):
    Category.objects.get(id = cid).delete()
    return redirect("manageCategory")

def ManageSubCategory(request):
    pass

def ManageProduct(request):
    d = {'title':'Manage Product'}
    products = Product.objects.all()
    subCat = SubCategory.objects.all()
    d.update({'products':products, 'subCat':subCat})
    if 'addproduct' in request.POST:
        print("In POST")
        n = request.POST['name']
        sc = request.POST['subCat']
        sc = SubCategory.objects.get(id = sc)
        dis = request.POST['dis']
        mrp = request.POST['mrp']
        sp = request.POST['sp']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']
        Product.objects.create(sub_cat = sc, name = n, discription = dis, mrp = mrp, sp = sp, img1 = img1, img2 = img2, img3 = img3)
    return render(request, 'manageProduct.html',d)

def HandelContactForm(request):
    pass


def EditProduct(request, pid):
    d = {'title':'Edit Product'}
    product = Product.objects.filter(id = pid).first()
    subCat = SubCategory.objects.all()
    d.update({'product':product, 'subCat':subCat})
    if 'editproduct' in request.POST:
        print("Inside Product") 
        product = Product.objects.filter(id = pid).first()
        n = request.POST['name']
        sc = request.POST['subCat']
        sc = SubCategory.objects.get(id = sc)
        dis = request.POST['dis']
        mrp = request.POST['mrp']
        sp = request.POST['sp']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']
        product.sub_cat = sc 
        product.name = n
        product.discription = dis 
        product.mrp = mrp
        product.sp = sp
        product.img1 = img1
        product.img2 = img2
        product.img3 = img3
        product.save()
        return redirect('manageProduct')
    return render(request,'editProduct.html',d)