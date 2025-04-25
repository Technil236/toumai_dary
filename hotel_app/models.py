from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class HotelAmenity(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font awesome icon class")
    
    def __str__(self):
        return self.name

class HotelImage(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotels/images/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.caption or f"Image {self.id}"

class Hotel(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=200)
    description = models.TextField()
    stars = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    amenities = models.ManyToManyField(HotelAmenity)
    cover_image = models.ImageField(upload_to='hotels/covers/')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    available_rooms = models.PositiveIntegerField()
    images = models.ManyToManyField(HotelImage)
    
    def __str__(self):
        return f"{self.name} at {self.hotel.name}"

class SpecialOffer(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='special_offers')
    title = models.CharField(max_length=200)
    description = models.TextField()
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} - {self.hotel.name}"