from django import forms

class TicketValidationForm(forms.Form):
    ticket_code = forms.CharField(max_length=5)
