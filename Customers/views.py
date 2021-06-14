from django.shortcuts import render, redirect
from Management.models import *
from .models import *
from Management.views import commonData
import requests
import json
from django.http import HttpResponse

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

headers = {"X-Api-Key": "",
           "X-Auth-Token": ""}

def Payment(request):
    mob = UserDetail.objects.get(user=request.user).mob
    cart = Cart.objects.filter(user = request.user)
    total = 0
    for i in cart:
        total += i.product.sp
    purp = "Payment for FashionHub"
    payload = {
        "purpose":purp,
        "amount":total,
        "buyer_name":str(request.user),
        "email":str(request.user.email),
        "phone":mob,
        "send_email":True,
        "send_sms":True,
        "redirect_url":"http://127.0.0.1:8000/payment_check/"
    }
    response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data = payload, headers = headers)
    print(response)
    y = response.text
    d = json.loads(y)
    print(d)
    a = d['payment_request']['longurl']
    i = d['payment_request']['id']
    Payment_ids.objects.create(ids = i,user = request.user)
    return redirect(a)

def payment_check(request):
    i = Payment_ids.objects.filter(user = request.user).first()
    ii = i.ids
    response = requests.get("https://www.instamojo.com/api/1.1/payment-requests/"+ str(ii)+'/', headers=headers)
    y = response.text
    b = json.loads(y)
    print(b)
    status = b['payment_request']['status']
    if status == "Sent":
        Cart.objects.filter(user = request.user).delete()
        return redirect('usercart')
    else:
        return HttpResponse("Payment Failed")
