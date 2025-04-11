from django.contrib import admin
from .models import TouristSite, TouristSiteCategory, TouristSiteImage

class TouristSiteImageInline(admin.TabularInline):
    model = TouristSiteImage
    extra = 1

@admin.register(TouristSite)
class TouristSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'city', 'entrance_fee', 'is_featured')
    list_filter = ('category', 'city', 'is_featured')
    search_fields = ('name', 'description')
    inlines = [TouristSiteImageInline]
    raw_id_fields = ('manager',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(manager=request.user)

@admin.register(TouristSiteCategory)
class TouristSiteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(TouristSiteImage)