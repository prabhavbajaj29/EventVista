


from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'performer_name',
            'event_date',
            'event_time',
            'ticket_price',
            'event_image',
        ]

