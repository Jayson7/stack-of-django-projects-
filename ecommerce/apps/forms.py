from django import forms
from django.db.models.base import Model
from django.forms import fields, forms
from django.forms.models import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    
    class Meta:
        
        model = Contact
        fields = "__all__"