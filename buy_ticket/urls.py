from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list_view, name='event_list'),
    path('buy/<int:event_id>/', views.ticket_purchase_view, name='ticket_purchase'),
    path('success/<int:ticket_id>/', views.ticket_success_view, name='ticket_success'),
]
