from django import forms

class TotalSpaces(forms.Form):
    total_spaces = forms.IntegerField(label='total spaces')