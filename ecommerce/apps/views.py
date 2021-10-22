from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User 
from django.db.models import Sum 
from .forms import *
# Create your views here.
from django.contrib.auth.models import User

def homepage(request):
    context = {}

    all_cart_products = CartItem.objects.all()
    
    counter = all_cart_products.count()
    context["counter"] = counter
    # context = {}
    product = Product.objects.all()[:6]
    context["product"] = product
    return render(request, "index.html", context)

def productdetails(request, pk):
    context = {}
    
    all_cart_products = CartItem.objects.all()
    
    counter = all_cart_products.count()
    context["counter"]  = counter  
    
    context["product"] = Product.objects.filter(pk = pk)
    product_viewed = Product.objects.filter(pk=pk).get()
    
    
    product_viewed.view_count +=1
    product_viewed.save()
    return render(request, "productdetails.html", context)


def addtocart (request, pk):
    context ={}
    all_cart_products = CartItem.objects.all()
    
    counter = all_cart_products.count()
    context["counter"] = counter
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
        # product_of_cart_in_question_pk_all = CartItem.objects.filter(product=product_in_question).get()
        if product_of_cart_in_question_pk.exists():    
            product_of_cart_in_question_pk_all = CartItem.objects.filter(product=product_in_question).get()
            
            # product_of_cart_in_question_pk = CartItem.objects.filter(pk=pk)
            print(" jayson this shit is in cart")
            print(product_of_cart_in_question_pk)
            product_of_cart_in_question_pk_all.quantity +=1
            product_of_cart_in_question_pk_all.save()
            
            total_amount = product_of_cart_in_question_pk_all.quantity * product_in_question.discounted_price
        
            product_of_cart_in_question_pk_all.amount = total_amount
            product_of_cart_in_question_pk_all.save()
                
                
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
            product_of_cart_in_question_pk_all = CartItem.objects.filter(product=product_in_question).get()
            
            total_amount = product_of_cart_in_question_pk_all.quantity * product_in_question.discounted_price
            product_of_cart_in_question_pk_all.amount = total_amount
            product_of_cart_in_question_pk_all.save()
       
    else:
        pass
        
        
    return redirect("/")

# cart

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
def cart(request):
    product = Product.objects.all()
    
    all_cart_products = CartItem.objects.all()
   
    context = {}
    context['cart_products_all'] = all_cart_products 
    
    counter = all_cart_products.count()
    context["counter"] = counter
    
    try:
    
        context["grandtotal"] = list(all_cart_products.aggregate(Sum("amount")).values())[0]
    
        grandtotal = context["grandtotal"]
        try:
            grand_total_check_user = GrandTotal.objects.get().created_by
            print(grand_total_check_user)
            grand_total_all = GrandTotal.objects.filter(created_by=grand_total_check_user)
                
            if not grand_total_all.exists():
                
                grand_total_model =  GrandTotal(
                    created_by= request.user,
                    total = grandtotal,
                )
                grand_total_model.save()
            else:
                grand_total_all.delete()
                
                context["grandtotal"] = list(all_cart_products.aggregate(Sum("amount")).values())[0]
        
                grandtotal = context["grandtotal"]
                grand_total_check_user = GrandTotal.objects.get().created_by
                grand_total_all = GrandTotal.onbjects.filter(created_by=grand_total_check_user)
                
                grand_total_model =  GrandTotal(
                        created_by= request.user,
                        total = grandtotal,
                    )
                grand_total_model.save()
            
        except ObjectDoesNotExist:
            
                
            # grand_total_check_user = GrandTotal.objects.get().created_by
            # grand_total_all = GrandTotal.onbjects.filter(created_by=grand_total_check_user)
                
            # grand_total_all.delete()    
            context["grandtotal"] = list(all_cart_products.aggregate(Sum("amount")).values())[0]
            
            grandtotal = context["grandtotal"]
                
            grand_total_model =  GrandTotal(
                        created_by= request.user,
                        total = grandtotal,
                    )
            grand_total_model.save() 
            
    except IntegrityError:

        grandtotal =0    
        context["grandtotal"] = grandtotal 
    print(grandtotal)
    return render(request, "cart.html", context )

def contact(request):
    context = {}
      
    all_cart_products = CartItem.objects.all()
   
   
    context['cart_products_all'] = all_cart_products 
    
    counter = all_cart_products.count()
    context["counter"] = counter
    
    formss = ContactForm()
    if request.method == 'POST':
        formss = ContactForm(request.POST)
       
        
    
        if formss.is_valid:
            new_forms = formss.save(commit=False)
            new_forms.save()
            return redirect('/')
        else:
            print("you have started again abi")
            return render(request, "contact.html", context)
            
    context["formss"] = formss
    return render(request, "contact.html", context)


# register page

def register(request):
    context = {}
    forms = UserForm()
    context['form'] = forms
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            new_forms = forms.save(commit=False)
            new_forms.save()
            return redirect('/')
        else:
            print("you have started again abi")
            return render(request, "registration/register.html", context)
        
     
    return render(request, 'register.html', context)