from django.contrib import admin
from .models import Booking, HotelBooking, RestaurantBooking, EventBooking, TouristSiteBooking

class HotelBookingInline(admin.TabularInline):
    model = HotelBooking
    extra = 0
    readonly_fields = ('room_type', 'check_in_date', 'check_out_date', 'number_of_rooms')
    can_delete = False

class RestaurantBookingInline(admin.TabularInline):
    model = RestaurantBooking
    extra = 0
    readonly_fields = ('restaurant', 'booking_date', 'booking_time', 'number_of_people')
    can_delete = False

class EventBookingInline(admin.TabularInline):
    model = EventBooking
    extra = 0
    readonly_fields = ('event', 'number_of_tickets')
    can_delete = False

class TouristSiteBookingInline(admin.TabularInline):
    model = TouristSiteBooking
    extra = 0
    readonly_fields = ('site', 'visit_date', 'number_of_visitors')
    can_delete = False

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'booking_date', 'total_amount', 'is_paid')
    list_filter = ('is_paid', 'booking_date')
    search_fields = ('user__username', 'id')
    readonly_fields = ('booking_date', 'total_amount', 'payment_reference')
    inlines = [HotelBookingInline, RestaurantBookingInline, 
               EventBookingInline, TouristSiteBookingInline]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'room_type', 'check_in_date', 'check_out_date')
    list_filter = ('room_type__hotel',)
    raw_id_fields = ('booking', 'room_type')
    readonly_fields = ('booking', 'room_type', 'check_in_date', 'check_out_date')

@admin.register(RestaurantBooking)
class RestaurantBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'restaurant', 'booking_date', 'booking_time')
    list_filter = ('restaurant',)
    raw_id_fields = ('booking', 'restaurant')
    readonly_fields = ('booking', 'restaurant', 'booking_date', 'booking_time')

@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'event', 'number_of_tickets')
    list_filter = ('event',)
    raw_id_fields = ('booking', 'event')
    readonly_fields = ('booking', 'event', 'number_of_tickets')

@admin.register(TouristSiteBooking)
class TouristSiteBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'site', 'visit_date')
    list_filter = ('site',)
    raw_id_fields = ('booking', 'site')
    readonly_fields = ('booking', 'site', 'visit_date')