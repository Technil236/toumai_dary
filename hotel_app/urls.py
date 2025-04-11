from django.urls import path
from . import views

app_name = 'hotel_app'

urlpatterns = [
    path('', views.manager_dashboard, name='dashboard'),  # Root path for /hotels/
    path('signup/', views.manager_signup, name='manager_signup'),
    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('add/', views.add_hotel, name='add_hotel'),
    path('manage/<int:hotel_id>/', views.manage_hotel, name='manage_hotel'),
    path('room/delete/<int:room_id>/', views.delete_room, name='delete_room'),
]