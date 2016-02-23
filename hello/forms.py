from django.forms import ModelForm, TextInput, PasswordInput, RadioSelect
from django import forms
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','username','password','birth_date','gender','age')
        widgets = {
            'email': TextInput(attrs={'class' : 'input-large', 'placeholder': 'Email',}),
            'first_name': TextInput(attrs={'class' : 'input-small', 'placeholder': 'First Name', }),
            'last_name': TextInput(attrs={'class' : 'input-small','placeholder': 'Last Name',}),
            'username': TextInput(attrs={'class' : 'input-large','placeholder': 'Username',}),
            'password': PasswordInput(attrs={'class' : 'input-large','placeholder': 'Password 6-8 digits',}),
            'birth_date': TextInput(attrs={'class' : 'input-large','placeholder': 'Date of Birth: yyyy-mm-dd',}),
            'gender': RadioSelect(choices = (('male','Male'), ('female','Female'), ('other','Other'),)),
            'age': TextInput(attrs={'class' : 'input-large','placeholder': 'Age',}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class' : 'input-large','placeholder': 'Username',}))
    password = forms.CharField(max_length=8,required=True,widget=forms.PasswordInput(attrs={'class' : 'input-large','placeholder': 'Password',}))
    