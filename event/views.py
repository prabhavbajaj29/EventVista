from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def event_create_view(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to create an event.')
        return redirect('home')
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('event_success', event_id=event.id)  # Use URL pattern name for redirection
    else:
        form = EventForm()
    return render(request, 'event/event_create.html', {'form': form})  # Correct template path

def event_success_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event/event_success.html', {'event': event})  # Correct template path


