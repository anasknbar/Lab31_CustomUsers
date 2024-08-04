from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .models import Flight,Passenger,Airport
from .form import AddAirportForm,AddFlightForm,AddPassengerForm
# Create your views here.

class IndexPageView(TemplateView):
  template_name = 'flights/index.html'
  
class FlightsPageView(ListView):
  model = Flight
  template_name = 'flights/all_flights.html'
  context_object_name = 'flights'
  
  
class FlightDetalisView(DetailView):
  model = Flight
  template_name = 'flights/flight_details.html'
  context_object_name = 'flight_details'
  
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flight = self.get_object()  # Get the specific flight instance
        context['airports'] = Airport.objects.all()  # Add all airports
        context['passengers'] = flight.passenger.all()  # Add passengers related to the specific flight
        context['non_passengers'] =  Passenger.objects.exclude(flight=flight).all()
        return context
  
  ### this code return me all the passengers on all the flights
  
  # def get_context_data(self, **kwargs):
  #       context = super().get_context_data(**kwargs)
  #       context['airports'] = Airport.objects.all()  # Add the airports queryset to the context
  #       context['passengers'] = Passenger.objects.all()  # Add the passengers queryset to the context
  #       return context

def book(request,flight_id):
  if request.method == "POST":
    # Accessing the flight
    flight = Flight.objects.get(pk=flight_id)

    # Finding the passenger id from the submitted form data
    passenger_id = int(request.POST["passenger"])

    # Finding the passenger based on the id
    passenger = Passenger.objects.get(pk=passenger_id)

    # Add passenger to the flight
    passenger.flight.add(flight)

    # Redirect user to flight page
    return HttpResponseRedirect(reverse("flight_details", args=(flight.id,)))


class AddAirportView(CreateView):
    model = Airport
    form_class = AddAirportForm
    template_name = 'flights/add_airport.html'
    success_url = reverse_lazy('all_flights')
    
class AddFlightView(CreateView):
  model = Flight
  form_class = AddFlightForm
  template_name = 'flights/add_flight.html'
  success_url = reverse_lazy('all_flights')

class AddPassengerView(CreateView):
  model = Passenger
  form_class = AddPassengerForm
  template_name = 'flights/add_passenger.html'
  success_url = reverse_lazy('all_flights')