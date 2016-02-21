from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import User
from .forms import RegistrationForm

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

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

def submit(request):
    
    user = User(request.POST)
    u = User(email=request.POST.get('email'),
    		first_name=request.POST.get('first_name'),
    		last_name=request.POST.get('last_name'),
    		username=request.POST.get('username'),
    		password=request.POST.get('password'),
    		birth_date=request.POST.get('birth_date'),
    		gender=request.POST.get('gender'),
    		age=request.POST.get('age'),
		)
    user.save()
    return render(request, 'index.html')

    






