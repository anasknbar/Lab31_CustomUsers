from django import forms
from .models import Airport,Flight,Passenger

class AddAirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'
        
class AddFlightForm(forms.ModelForm):
  class Meta:
    model = Flight
    fields = '__all__'
    
class AddPassengerForm(forms.ModelForm):
  class Meta:
    model = Passenger
    fields = '__all__'



