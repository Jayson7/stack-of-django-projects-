import django.contrib.auth.urls
from django.contrib import admin
from django.urls import path, include
from apps import views 
from apps.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.homepage, name="home"),
    path('details/<int:pk>', views.productdetails, name="details"),
    path('admin/', admin.site.urls),
    path('cart', views.cart, name="cart"),
    path('addtocart/<int:pk>', views.addtocart, name="addtocart"),
    path('contact', views.contact, name="contact"),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name="register"),
    path('deletcart/<int:pk>', views.deletecart, name="deletecart"),
    path('clear', views.clearcart, name="clearcart"),
    path('profile', views.profilepage, name="profile"),
    
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
