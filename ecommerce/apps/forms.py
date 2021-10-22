
from django import forms
from django.db.models.base import Model
from django import  forms
from django.forms.models import ModelForm
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    
    class Meta:
        
        model = Contact
        fields = "__all__"
        
class UserForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    profile_picture = forms.ImageField()
    date_joined = forms.DateField(auto_now_add=True)
    phone_number = forms.IntegerField(max_length= 11, required = True)
    
    

    class Meta:
        
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name", "profile_picture", 'date_joined', "phone_number" )

            

        def save(self, commit=True):
            user = super(UserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.last_name = self.cleaned_data['last_name']
            user.first_name = self.cleaned_data['first_name']
            user.profile_picture = self.cleaned_data['profile_picture']
            user.date_joined = self.cleaned_data['date_joined']
            user.phone_number = self.cleaned_data['phone_number']
            
            
            if commit:
                user.save()
            return user