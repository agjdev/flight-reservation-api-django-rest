from django.shortcuts import render
from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework.viewsets import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','POST'])
def findFlights(request):
    flights = Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
    serializer = FlightSerializer(flights,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])
    
    
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.middleName = request.data['middleName']
    passenger.lastName = request.data['lastName']
    passenger.phoneNumber = request.data['phoneNumber']
    passenger.email = request.data['email']
    passenger.save()
    
    
    reservation =  Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    
    
    Reservation.save()
    return Response(status=status.HTTP_201_CREATED) 
    
class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]
    
class PassengerViewSet(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer    
    
class ReservationViewSet(ModelViewSet):  
        queryset = Reservation.objects.all()
        serializer_class = ReservationSerializer     