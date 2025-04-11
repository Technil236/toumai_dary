'''
from django.contrib import admin
from .models import Hotel, Restaurant

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'rating', 'localisation', 'tel', 'email', 'admin_user')
    search_fields = ('nom', 'localisation')
    list_filter = ('rating',)

    def get_queryset(self, request):
        # Restrict hotel admins to only see their own hotel
        queryset = super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            return queryset.filter(admin_user=request.user)
        return queryset

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'email','admin_user')
    search_fields = ('nom', 'adresse')
    list_filter = ('rating',)


    def get_queryset(self, request):
        # Restrict restaurant admins to only see their own restaurant
        queryset = super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            return queryset.filter(admin_user=request.user)
        return queryset

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
'''

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 
                   'is_hotel_owner', 'is_restaurant_owner', 
                   'is_event_organizer', 'is_tourist_site_manager',
                   'is_staff')
    
    # Fields to filter by in the right sidebar
    list_filter = ('is_hotel_owner', 'is_restaurant_owner', 
                  'is_event_organizer', 'is_tourist_site_manager',
                  'is_staff', 'is_superuser', 'is_active')
    
    # Fieldsets for the edit view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Business Roles', {
            'fields': ('is_hotel_owner', 'is_restaurant_owner', 
                      'is_event_organizer', 'is_tourist_site_manager'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )

# Unregister the default User admin if it's registered
# Only needed if you're replacing the default User model
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register your custom User model with the custom admin
admin.site.register(User, CustomUserAdmin)