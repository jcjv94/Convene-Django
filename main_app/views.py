from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from .models import Event

# Create your views here.


class EventCreate(CreateView):
    model = Event
    fields = ['title', 'date', 'time', 'location', 'description', 'attendees', 'infolink']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
     
def landing(request):
    return render(request, 'index.html', {'arr' : ['Outdoors', 'Music', 'Food','Tech','Education']})

def add_event(request):
    form = PostForm()
    return render(request, 'add_event.html', {'form': form})

def user(request):
    return render(request, 'user/profile.html')

def events(request):
    return render(request, 'events/index.html')

