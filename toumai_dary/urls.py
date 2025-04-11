# toumai_dary/urls.py
from django.contrib import admin
from django.urls import path, include
from hotel_app.views import hotels_home  # or wherever your homepage view is

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', include('hotel_app.urls')),
    path('', hotels_home, name='home'),  
    path('accounts/', include('django.contrib.auth.urls')),  # 👈 This line

]
