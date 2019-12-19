from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm
from .models import Event
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    form = PostForm(request.POST)
    print(form)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.save()
    return render(request, 'add_event.html', {'form': form})

def user(request):
    return render(request, 'user/profile.html')

def events(request):
    return render(request, 'events/index.html')


def signup(request):
    error_message = ''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign up - Try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
