from django import forms

from .models import Event

class TotalSpaces(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    available_spaces = forms.IntegerField(label='Available Spaces (Standard)')
    available_spaces_lrg = forms.IntegerField(label='Available Spaces (Large)')
    location = forms.CharField(label='Location', max_length=10000)
    nickname = forms.CharField(label='Name', max_length=10000)
    price = forms.IntegerField(label='Price')

class SignUp(forms.Form):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
