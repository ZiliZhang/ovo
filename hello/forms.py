from django import forms

class RegistrationForm(forms.Form):
    email = forms.CharField(max_length=50,required=True, widget=forms.TextInput(attrs={'class' : 'input-large', 'placeholder': 'Email',}))
    first_name = forms.CharField(max_length=30,required=True, widget=forms.TextInput(attrs={'class' : 'input-small', 'placeholder': 'First Name', }))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'input-small','placeholder': 'Last Name',}))
    username = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class' : 'input-large','placeholder': 'Username',}))
    password = forms.CharField(max_length=8,required=True,widget=forms.PasswordInput(attrs={'class' : 'input-large','placeholder': 'Password 6-8 digits',}))
    birth_date = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class' : 'input-large','placeholder': 'Date of Birth: yyyy-mm-dd',}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = (('male','Male'), ('female','Female'), ('other','Other'),))
    # gender = forms.CharField(max_length=10)
    age = forms.IntegerField(min_value=0,required=True,widget=forms.TextInput(attrs={'class' : 'input-large','placeholder': 'Age',}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class' : 'input-large','placeholder': 'Username',}))
    password = forms.CharField(max_length=8,required=True,widget=forms.PasswordInput(attrs={'class' : 'input-large','placeholder': 'Password',}))
    