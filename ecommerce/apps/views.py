from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 

# Create your views here.

def homepage(request):
    context = {}
    product = Product.objects.all()
    context["product"] = product
    return render(request, "index.html", context)

def productdetails(request, pk):
    
    context = {}
    context["product"] = Product.objects.filter(pk = pk)
    
    return render(request, "productdetails.html", context)

def addtocart (request, pk):
    cartmainmodel = Cart
    cartitemall = CartItem.objects.all()
    products = Product 
    productall = Product.objects.all()
    if request.user.is_authenticated:
        print("sent in a product")
        product_in_question = Product.objects.filter(pk=pk)
        print(product_in_question)
        # print(product_in_question) 
        print(product_in_question)
        cart_item_in_question = CartItem(
            created_by = request.user,
            product = product_in_question,
            # amount = 
        )    
        cart_item_in_question.save()
        
        # cart_item_in_question.created_by([request.user])
        # cart_item_in_question.product.set(product_in_question)
        # cart_item_in_question.save()
    else:
        
        pass
        
    return redirect("/")

def cart(request):
    context = {}
    context["cartmainmodel"] = Cart
    context["cartitemall"] = CartItem.objects.all()
    context["cart"] = Cart.objects.all()    
    products = Product 
    productall = Product.objects.all()
   
    
    return render(request, "cart.html", context)