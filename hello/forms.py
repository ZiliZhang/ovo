from django import forms

class RegistrationForm(forms.Form):
    email = forms.CharField(max_length=50,required=True)
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=8,required=True)
    birth_date = forms.CharField(max_length=10)
    gender = forms.CharField(max_length=6)
    age = forms.IntegerField(min_value=0,required=True)