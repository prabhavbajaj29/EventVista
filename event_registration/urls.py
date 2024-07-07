from django.urls import path
from . import views

urlpatterns = [
    path('validate/', views.validate_ticket_view, name='validate_ticket'),
]
