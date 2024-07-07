from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('create/', views.event_create_view, name='event_create'),
    path('success/<int:event_id>/', views.event_success_view, name='event_success'),
    
    
    
]
