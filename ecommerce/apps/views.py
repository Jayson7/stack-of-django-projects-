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
        product_in_question_pk = Product.objects.filter(pk=pk)
        product_in_question = Product.objects.filter(pk=pk).get()
        # print(cartitemall)
        # print(product_in_question)
        product_of_cart_in_question_pk = CartItem.objects.filter(product=product_in_question)
        
        if product_of_cart_in_question_pk.exists():    
            # product_of_cart_in_question_pk = CartItem.objects.filter(pk=pk)
            print(" jayson this shit is in cart")
            print(product_of_cart_in_question_pk)
            
            # cart_item_in_question.save()
            # pass
    
        if not product_of_cart_in_question_pk.exists():
            
            
            print(product_in_question.discounted_price)
            # print(product_in_question) 
            print(product_in_question)
            cart_item_in_question = CartItem(
                created_by = request.user,
                product = product_in_question,
                amount = product_in_question.discounted_price,
                quantity = 1,
            ).save()
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