
from django.contrib import admin
from django.urls import path
from apps import views
from apps.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),

]
