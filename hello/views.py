from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import User
from .forms import RegistrationForm
from .forms import LoginForm
# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # print "hi\n"
            return HttpResponseRedirect('/')
    #Get Request            
    else:
        form = LoginForm()
    return render(request, 'index.html',{'lform': form})

def reg(request):
    #return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

    	    return HttpResponseRedirect('/')
    #Get Request    	    
    else:
	    form = RegistrationForm()
    return render(request, 'reg.html',{'form': form})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    user = User()
    user.save()

    users = User.objects.all()

    return render(request, 'db.html', {'greetings': greetings}, {'users': users})


    






