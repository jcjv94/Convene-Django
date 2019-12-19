from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing(request):
    return render(request, 'home.html')

def auth(request):
    return render(request, 'auth.html')

def user(request):
    return render(request, 'user/profile.html')

def events(request):
    return render(request, 'events/index.html')