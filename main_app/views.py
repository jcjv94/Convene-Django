from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Event
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class EventCreate(CreateView):
    model = Event
    fields = ['title', 'date', 'time', 'location',
              'description', 'attendees', 'infolink']

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super().form_valid(form)


def events_index(request):
    #   events = Event.objects.filter()
    #   events = request.user.event_set.all()
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})


def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    # Instantiate FeedingForm to be rendered in the template
    post_form = PostForm()
    return render(request, 'events/detail.html', {
        # Pass the cat and feeding_form as context
        'event': event
    })


def landing(request):
    return render(request, 'index.html', {'arr': ['Outdoors', 'Entertainment', 'Food', 'Tech', 'Education', 'Health']})


def user(request):
    return render(request, 'user/profile.html')


def events(request):
    return render(request, 'events/index.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Sign up - Try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
