from django.db import models
from django.contrib.auth import get_user_model
from event.models import Event
import string
import random

def generate_unique_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

User = get_user_model()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    unique_code = models.CharField(max_length=5, unique=True, default=generate_unique_code)

    def __str__(self):
        return f'{self.user.username} - {self.event.event_name} - {self.unique_code}'
