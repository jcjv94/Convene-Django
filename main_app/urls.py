from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import render


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


urlpatterns = [
    path('', views.landing, name='landing'),
    path('auth/', views.auth, name='auth'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout_view, name='logout'),
]
