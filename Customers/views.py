from django.shortcuts import render, redirect
from Management.models import *
from .models import *
from Management.views import commonData

def ProductsPage(request, cid):
    d = {"title":"Shoping Page"}
    products = Product.objects.filter(sub_cat__cat__id = cid)
    d.update(commonData())
    d.update({'products': products})
    return render(request,'productspage.html', d)

def SingleProduct(request,pid):
    d = {"title":"Shoping Page"}
    product = Product.objects.filter(id = pid).first()
    d.update(commonData())
    d.update({'pr': product})
    return render(request,'singleProduct.html', d)

def AddToCart(request, pid):
    product = Product.objects.filter(id = pid).first()
    Cart.objects.create(user = request.user, product = product)
    return redirect('home')

def UserCart(request):
    d = {"title":"Cart"}
    cart = Cart.objects.filter(user = request.user)
    d.update(commonData())
    d.update({'cart': cart})
    total = 0
    for i in cart:
        total += i.product.sp
    d.update({'total': total})
    return render(request, 'Cart.html', d)


