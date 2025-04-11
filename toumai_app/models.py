'''
from django.db import models
from django.contrib.auth.models import User

class Evenement(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    organisateur = models.CharField(max_length=255)
    description = models.TextField()
    dateDebut = models.DateField()
    dateFin = models.DateField()
    tarif = models.FloatField()

    def __str__(self):
        return self.nom


class Touriste(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    nationalite = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Hotel(models.Model):
    RATING_CHOICES = [
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
    ]    
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    localisation = models.CharField(max_length=255)
    tel = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom


class SiteTouristique(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    localisation = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nom


class Restaurant(models.Model):
    RATING_CHOICES = [
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
    ]

    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom


class Service(models.Model):
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return f"Service {self.id}"


class Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    numero = models.CharField(max_length=50)
    localisation = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    nationalite = models.CharField(max_length=100)

    def __str__(self):
        return self.numero
    
class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    touriste = models.ForeignKey(Touriste, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, null=True, blank=True, on_delete=models.SET_NULL)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.SET_NULL)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.SET_NULL)
    table = models.ForeignKey(Table, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    time = models.TimeField()
    confirmed = models.BooleanField(default=False)

class Review(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    id = models.BigAutoField(primary_key=True)
    touriste = models.ForeignKey(Touriste, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.touriste.nom} - {self.get_rating_display()}"
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_hotel_owner = models.BooleanField(default=False)
    is_restaurant_owner = models.BooleanField(default=False)
    is_event_organizer = models.BooleanField(default=False)
    is_tourist_site_manager = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'auth_user'
        app_label = 'toumai_app'  
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    class Meta:
        abstract = True