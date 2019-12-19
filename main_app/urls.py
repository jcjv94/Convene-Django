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
    path('events/<int:event_id>/', views.events_detail, name='detail'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('user/', views.user, name='user'),
    path('events/', views.events, name='events'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout_view, name='logout'),
]
