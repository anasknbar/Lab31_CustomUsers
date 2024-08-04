from django.urls import path
from .views import IndexPageView,FlightsPageView,FlightDetalisView,AddAirportView,AddFlightView,AddPassengerView
from . import views

urlpatterns = [
  path('',IndexPageView.as_view(),name = 'home'),
  path('all_flights',FlightsPageView.as_view(),name = 'all_flights'),
  path('flight_details/<int:pk>',FlightDetalisView.as_view(),name="flight_details"),
  path('<int:flight_id>/book',views.book,name='book'),
  
  path('add_airport/',AddAirportView.as_view(),name='add_airport'),
  path('add_flight/',AddFlightView.as_view(),name='add_flight'),

  path('add_passenger/', AddPassengerView.as_view(), name='add_passenger'),


]