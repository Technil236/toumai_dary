from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel, RoomType
from .forms import HotelForm, RoomTypeForm
from django.http import HttpResponseForbidden

def manager_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_hotel_owner = True 
            user.save()
            login(request, user)
            return redirect('hotel_app:manager_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'hotel_app/manager_signup.html', {'form': form})


@login_required
def manager_dashboard(request):
    if not getattr(request.user, 'is_hotel_owner', False):
        return HttpResponseForbidden("Access Denied")

    hotels = Hotel.objects.filter(owner=request.user)
    return render(request, 'hotel_app/manager_dashboard.html', {'hotels': hotels})


@login_required
def add_hotel(request):
    if not getattr(request.user, 'is_hotel_owner', False):
        return HttpResponseForbidden("Access Denied")

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.owner = request.user
            hotel.save()
            form.save_m2m()
            return redirect('hotel_app:manager_dashboard')
    else:
        form = HotelForm()

    return render(request, 'hotel_app/hotel_form.html', {'form': form})


@login_required
def manage_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id, owner=request.user)

    if request.method == 'POST':
        room_form = RoomTypeForm(request.POST, request.FILES)
        if room_form.is_valid():
            room = room_form.save(commit=False)
            room.hotel = hotel
            room.save()
            room_form.save_m2m()
            return redirect('hotel_app:manage_hotel', hotel_id=hotel.id)
    else:
        room_form = RoomTypeForm()

    room_types = RoomType.objects.filter(hotel=hotel)
    return render(request, 'hotel_app/manage_hotel.html', {
        'hotel': hotel,
        'room_form': room_form,
        'room_types': room_types
    })


@login_required
def delete_room(request, room_id):
    room = get_object_or_404(RoomType, id=room_id, hotel__owner=request.user)
    hotel_id = room.hotel.id
    room.delete()
    return redirect('hotel_app:manage_hotel', hotel_id=hotel_id)

def hotels_home(request):
    return render(request, 'hotel_app/base.html')

# hotel_app/views.py
def hotels_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_app/hotels_list.html', {'hotels': hotels})
