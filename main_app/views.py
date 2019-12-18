from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'auth.html')

