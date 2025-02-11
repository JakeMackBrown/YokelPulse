from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)  # Visibility field
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)  # Updated field for event image

    def __str__(self):
        return self.title

class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_rsvpd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} RSVPed to {self.event.title}'