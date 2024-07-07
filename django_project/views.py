from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from event.models import Event
from buy_ticket.models import Ticket

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'website/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
      logout(request)
      return redirect('home')

@login_required
def profile_view(request):
  if request.user.is_superuser:  # Check if user is admin
      created_events = Event.objects.all()  # Show all events to admin
      bought_tickets = Ticket.objects.all()  # Show all tickets to admin
      return render(request, 'website/profile_admin.html', {'created_events': created_events, 'bought_tickets': bought_tickets})
  else:
      bought_tickets = Ticket.objects.filter(user=request.user)
      return render(request, 'website/profile_user.html', {'bought_tickets': bought_tickets})




def home(request):
  #return HttpResponse("Welcome at home page")
  return render(request,'website/base.html')