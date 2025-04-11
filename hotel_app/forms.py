from django import forms
from .models import Hotel, RoomType

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'description', 'stars', 'amenities', 'cover_image', 
                 'is_featured', 'opening_time', 'closing_time']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name', 'description', 'price_per_night', 'capacity', 
                 'available_rooms', 'images']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price_per_night': forms.NumberInput(attrs={'step': '0.01'}),
        }