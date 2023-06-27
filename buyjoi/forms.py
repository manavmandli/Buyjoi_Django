from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms



class CustomUserForm(UserCreationForm):
    first_name = forms.CharField( widget= forms.TextInput( attrs={'class' : 'text-sm placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400' , 'placeholder' : 'Enter your first name' }))
    last_name = forms.CharField( widget= forms.TextInput( attrs={'class' : 'text-sm placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400' , 'placeholder' : 'Enter your last name' }))
    username = forms.CharField( widget= forms.TextInput( attrs={'class' : 'text-sm placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400' , 'placeholder' : 'Enter your username' }))
    email = forms.CharField( widget= forms.TextInput( attrs={'class' : 'text-sm placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400' , 'placeholder' : 'Enter your email' }))
    password1 = forms.CharField( widget= forms.PasswordInput( attrs={'class' : 'text-sm placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400' , 'placeholder' : 'Enter your password' }))
    password2 = forms.CharField( widget= forms.PasswordInput( attrs={'class' : 'text-sm placeholder-gray-500 pl-10 pr-4 rounded-2xl border border-gray-400 w-full py-2 focus:outline-none focus:border-blue-400' , 'placeholder' : 'Confirm your password' }))
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']