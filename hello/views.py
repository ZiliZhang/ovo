from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def reg(request):
    #return HttpResponse('Hello from Python!')
    return render(request, 'reg.html')


def db(request):

    user = User()
    user.save()

    users = User.objects.all()

    return render(request, 'db.html', {'users': users})

