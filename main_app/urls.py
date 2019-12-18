from django.urls import path 
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('auth/', views.auth, name='auth'),
]
