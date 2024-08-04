from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
  list_display = ("id", "origin", "destination", "duration")
class AirportAdmin(admin.ModelAdmin):
  list_display = ("city","code")

# I can not show this on the admin Interface, because of the mant-to-many releation
# many-to-many releations has special display attributes  
class PassengerAdmin(admin.ModelAdmin):
  filter_horizontal = ("flight",)
    
admin.site.register(Flight,FlightAdmin)
admin.site.register(Airport,AirportAdmin)
admin.site.register(Passenger,PassengerAdmin)