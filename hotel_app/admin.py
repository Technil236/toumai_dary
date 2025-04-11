from django.contrib import admin
from .models import Hotel, HotelAmenity, RoomType, HotelImage, SpecialOffer

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1
    fields = ('image', 'caption')

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1
    show_change_link = True

class SpecialOfferInline(admin.TabularInline):
    model = SpecialOffer
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'stars', 'is_featured')
    list_filter = ('stars', 'is_featured')
    search_fields = ('name', 'description')
    inlines = [HotelImageInline, RoomTypeInline, SpecialOfferInline]
    filter_horizontal = ('amenities',)

@admin.register(HotelAmenity)
class HotelAmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'price_per_night', 'available_rooms')
    list_filter = ('hotel',)
    search_fields = ('name', 'hotel__name')

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'hotel', 'discount_percentage', 'is_active')
    list_filter = ('is_active', 'hotel')
    search_fields = ('title', 'hotel__name')