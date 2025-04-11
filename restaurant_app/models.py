from django.db import models
from django.conf import settings
from toumai_app.models import Location

class Restaurant(Location):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=200)
    description = models.TextField()
    cuisine_type = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='restaurants/covers/')
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'
    
    def __str__(self):
        return self.name

class DishCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Dish Category'
        verbose_name_plural = 'Dish Categories'
        unique_together = ('restaurant', 'name')
    
    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

class Dish(models.Model):
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='restaurants/dishes/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ['category', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.category.restaurant.name}"

class RestaurantSpecialOffer(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='special_offers')
    title = models.CharField(max_length=200)
    description = models.TextField()
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Special Offer'
        verbose_name_plural = 'Special Offers'
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} ({self.restaurant.name})"