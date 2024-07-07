from django.shortcuts import render
from django.http import HttpResponse
from buy_ticket.models import Ticket
from .forms import TicketValidationForm

def validate_ticket_view(request):
    if request.method == 'POST':
        form = TicketValidationForm(request.POST)
        if form.is_valid():
            ticket_code = form.cleaned_data['ticket_code']
            try:
                ticket = Ticket.objects.get(unique_code=ticket_code)
                return render(request, 'event_registration/validation_success.html', {'ticket': ticket})
            except Ticket.DoesNotExist:
                return render(request, 'event_registration/validation_fail.html', {'error': 'Invalid ticket code'})
    else:
        form = TicketValidationForm()
    return render(request, 'event_registration/validate_ticket.html', {'form': form})
