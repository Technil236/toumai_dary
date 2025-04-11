from django.contrib import admin
from .models import Event, EventCategory, EventImage

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date', 'ticket_price', 'available_tickets', 'is_featured')
    list_filter = ('category', 'start_date', 'is_featured')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    inlines = [EventImageInline]
    raw_id_fields = ('organizer',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(organizer=request.user)

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(EventImage)