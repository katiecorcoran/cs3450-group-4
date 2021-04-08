from django import forms

class TotalSpaces(forms.Form):
    available_spaces = forms.IntegerField(label='available spaces (regular)')
    available_spaces_lrg = forms.IntegerField(label='available spaces large')
    location = forms.CharField(label='location', max_length=10000)
    nickname = forms.CharField(label='Name of lot', max_length=10000)
    total_spaces = forms.IntegerField(label='Total spaces')

class SignUp(forms.Form):
    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
