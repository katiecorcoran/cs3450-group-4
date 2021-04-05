from django import forms

class TotalSpaces(forms.Form):
    total_spaces = forms.IntegerField(label='Total spaces')

class SignUp(forms.Form):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
