
from django.contrib import admin
from django.urls import path
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
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
