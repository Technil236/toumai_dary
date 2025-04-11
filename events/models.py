from django.db import models
from toumai_app.models import User, Location
from django.conf import settings

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Event(Location):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    cover_image = models.ImageField(upload_to='events/covers/')
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available_tickets = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events/images/')
    caption = models.CharField(max_length=200, blank=True)