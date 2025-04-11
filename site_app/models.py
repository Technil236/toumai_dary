from django.db import models
from toumai_app.models import User, Location
from django.conf import settings


class TouristSiteCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class TouristSite(Location):
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tourist_sites')
    category = models.ForeignKey(TouristSiteCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    entrance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cover_image = models.ImageField(upload_to='tourist_sites/covers/')
    is_featured = models.BooleanField(default=False)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class TouristSiteImage(models.Model):
    site = models.ForeignKey(TouristSite, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tourist_sites/images/')
    caption = models.CharField(max_length=200, blank=True)