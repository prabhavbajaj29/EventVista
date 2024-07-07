# models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    performer_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    event_image = models.ImageField(upload_to='event_images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.event_name
