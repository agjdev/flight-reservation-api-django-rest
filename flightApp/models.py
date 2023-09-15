from django.db import models

# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=10)
    arrivalCity = models.CharField(max_length=10)
    dateOfDeparture = models.DateField()
    estTimeOfDeparture = models.TimeField()
    


class Passenger(models.Model):
    firstName = models.CharField(max_length=10)
    middleName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=10)
 
 
class Reservation(models.Model):
     flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
     passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)
     
     def __str__(self):
         return self.flight + self.passenger
     