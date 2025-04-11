from django.contrib import admin
from .models import Restaurant, DishCategory, Dish, RestaurantSpecialOffer

class DishCategoryInline(admin.TabularInline):
    model = DishCategory
    extra = 1
    show_change_link = True

class DishInline(admin.TabularInline):
    model = Dish
    extra = 1
    fields = ('name', 'price', 'is_available', 'image')
    show_change_link = True

class SpecialOfferInline(admin.TabularInline):
    model = RestaurantSpecialOffer
    extra = 1
    fields = ('title', 'discount_percentage', 'is_active')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine_type', 'owner', 'is_featured', 'opening_time', 'closing_time')
    list_filter = ('cuisine_type', 'is_featured')
    search_fields = ('name', 'description', 'cuisine_type')
    inlines = [DishCategoryInline, SpecialOfferInline]
        
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    list_filter = ('restaurant',)
    search_fields = ('name', 'restaurant__name')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__owner=request.user)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('is_available', 'category__restaurant')
    search_fields = ('name', 'description', 'category__name')
    raw_id_fields = ('category',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(category__restaurant__owner=request.user)

@admin.register(RestaurantSpecialOffer)
class RestaurantSpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'restaurant', 'discount_percentage', 'is_active', 'start_date', 'end_date')
    list_filter = ('is_active', 'restaurant')
    search_fields = ('title', 'restaurant__name')
    date_hierarchy = 'start_date'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(restaurant__owner=request.user)