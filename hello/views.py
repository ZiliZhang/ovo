from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import User

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def reg(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'reg.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    user = User()
    user.save()

    users = User.objects.all()

    return render(request, 'db.html', {'greetings': greetings}, {'users': users})

