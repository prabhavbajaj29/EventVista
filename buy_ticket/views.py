from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from event.models import Event
from .models import Ticket
from .forms import TicketForm

def event_list_view(request):
    events = Event.objects.all()
    return render(request, 'buy_ticket/event_list.html', {'events': events})

@login_required
def ticket_purchase_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.event = event
            ticket.save()
            return redirect('ticket_success', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'buy_ticket/ticket_purchase.html', {'event': event, 'form': form})

def ticket_success_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'buy_ticket/ticket_success.html', {'ticket': ticket})
