from Doctor.views import booking_view, bookings_list_view
from django.urls import path

urlpatterns = [
    path('appointment', booking_view, name='Booking_view'),
    path('Bookings_list', bookings_list_view, name='Bookings_list_view'),
]