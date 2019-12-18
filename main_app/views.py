from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def landing(request):
     

    return render(request, 'index.html')

def auth(request):
    return render(request, 'auth.html')

