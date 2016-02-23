from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import User
from .forms import UserForm
from .forms import LoginForm
# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    #Get Request            
    else:
        form = LoginForm()
    return render(request, 'index.html',{'lform': form})

def reg(request):
    #return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user_entry = form.save()
    	    return HttpResponseRedirect('success.html')
    #Get Request    	    
    else:
	    form = UserForm()
    return render(request, 'reg.html',{'form': form})

def success(request):
    return render(request, 'success.html')


