from django.contrib import admin
from .models import Event, RSVP  # Import RSVP model

# Register your models here.
admin.site.register(Event)
admin.site.register(RSVP)  # Register RSVP model
