from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User 
from django.db.models import Sum 
from .forms import *
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# home page config
def homepage(request):

    context = {}

    all_cart_products = CartItem.objects.all()
    if request.user.is_authenticated:
            
        counter = all_cart_products.count()
        context["counter"] = counter
    else:
        pass
    # context = {}
    product = Product.objects.all()[:6]
    context["product"] = product
    return render(request, "index.html", context)

# product details view
# login is requried

@login_required(login_url='/login/')
def productdetails(request, pk):
    context = {}
    
    all_cart_products = CartItem.objects.all()
    
    if request.user.is_authenticated:
            
        counter = all_cart_products.count()
        context["counter"] = counter
    else:
        pass
    context["product"] = Product.objects.filter(pk = pk)
    product_viewed = Product.objects.filter(pk=pk).get()
    
    
    product_viewed.view_count +=1
    product_viewed.save()
    return render(request, "productdetails.html", context)


# add to cart view controller 

@login_required(login_url='/login/')
def addtocart (request, pk):
    context ={}
    all_cart_products = CartItem.objects.all()
    
    if request.user.is_authenticated:
            
        counter = all_cart_products.count()
        context["counter"] = counter
    else:
        pass
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

@login_required(login_url='/login/')
def cart(request):
    product = Product.objects.all()
    
    all_cart_products = CartItem.objects.all()
   
    context = {}
    context['cart_products_all'] = all_cart_products 
    
    if request.user.is_authenticated:
            
        counter = all_cart_products.count()
        context["counter"] = counter
    else:
        pass
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

#  delete cart item view
def deletecart(request, pk):
    
    cartitem = CartItem.objects.all()
    cartitem_pk = cartitem.filter(pk=pk)
    print(cartitem_pk)
    cartitem_pk.delete()
    
    return redirect("cart")

# clear cart view 

def clearcart(request):
    
    cartitem = CartItem.objects.all()
    
    print(cartitem)
    cartitem.delete()
    
    return redirect("cart")


# contact view

def contact(request):
    context = {}
      
    all_cart_products = CartItem.objects.all()
   
   
    context['cart_products_all'] = all_cart_products 
    
    if request.user.is_authenticated:
            
        counter = all_cart_products.count()
        context["counter"] = counter
    else:
        pass
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
    formss = UserForm()
    
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            new_forms = forms.save(commit=False)
            new_forms.save()
            messages.success(request, 'Your account has been created successfully!')
        else:
            print(forms.errors)
            messages.error(request, 'WTF!')
            context['errors'] = forms.errors 
            print("you have started again abi")
            # return HttpResponse(forms.errors.values())
        
    context['formss'] = formss 
    return render(request, 'registration/register.html', context)

# profile page for all users 
def profilepage(request):
    usernames = request.user
    context = {}
    check = User.objects.filter(username=usernames).get()
    print(check)
    context['check'] = check
    return render(request, 'profile.html', context )