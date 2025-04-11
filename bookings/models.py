from django.db import models
from toumai_app.models import User
from hotel_app.models import RoomType
from restaurant_app.models import Restaurant
from events.models import Event
from site_app.models import TouristSite
from django.conf import settings


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Booking #{self.id} by {self.user.username}"

class HotelBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='hotel_bookings')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_rooms = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    
    def __str__(self):
        return f"Hotel booking for {self.room_type.hotel.name}"

class RestaurantBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='restaurant_bookings')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_people = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    
    def __str__(self):
        return f"Restaurant booking at {self.restaurant.name}"

class EventBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='event_bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_tickets = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"Event booking for {self.event.title}"

class TouristSiteBooking(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='tourist_site_bookings')
    site = models.ForeignKey(TouristSite, on_delete=models.CASCADE)
    visit_date = models.DateField()
    number_of_visitors = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"Visit to {self.site.name}"