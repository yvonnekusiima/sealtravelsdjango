from django.db import models

# Create your models here.


# Administrator
class ADMINISTRATOR(models.Model):
    AdministratorId = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


class ADMINISTRATORACTIVITYLOG(models.Model):
    AdministratorId = models.CharField(max_length=50)
    DateTimestamp = models.CharField(max_length=50)
    Action = models.CharField(max_length=50)
    IPAddress = models.CharField(max_length=50)
    HostName = models.CharField(max_length=50)


# Users
class USERS(models.Model):
    Id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=100)
    DateAdded = models.CharField(max_length=50)


class USERACTIVITYLOG(models.Model):
    Username = models.CharField(max_length=50)
    DateTimestamp = models.CharField(max_length=50)
    Action = models.CharField(max_length=50)
    IPAddress = models.CharField(max_length=50)
    HostName = models.CharField(max_length=50)


# Flights
class ONEWAYFLIGHTS(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    TripType = models.CharField(max_length=50)
    LeavingFrom = models.CharField(max_length=50)
    GoingTo = models.CharField(max_length=50)
    Departing = models.CharField(max_length=50)
    Adults = models.CharField(max_length=50)
    Children = models.CharField(max_length=50)
    FlightType = models.CharField(max_length=50)
    Airline = models.CharField(max_length=50)
    TravelClass = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)


class ROUNDTRIPFLIGHTS(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    TripType = models.CharField(max_length=50)
    LeavingFrom = models.CharField(max_length=50)
    GoingTo = models.CharField(max_length=50)
    Departing = models.CharField(max_length=50)
    Returning = models.CharField(max_length=50)
    Adults = models.CharField(max_length=50)
    Children = models.CharField(max_length=50)
    FlightType = models.CharField(max_length=50)
    Airline = models.CharField(max_length=50)
    TravelClass = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)


class FLIGHTPAYMENTS(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    PaymentMethod = models.CharField(max_length=50)
    CardNumber = models.CharField(max_length=50)
    CVV = models.CharField(max_length=50)
    ExpiryDate = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)


class FLIGHTTICKETS(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    FlightNumber = models.CharField(max_length=50)
    TravelClass = models.CharField(max_length=50)
    CheckinOpens = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    Departure = models.CharField(max_length=50)
    Arrival = models.CharField(max_length=50)
    DepartingFrom = models.CharField(max_length=50)
    DepartureAirportandTerminal = models.CharField(max_length=50)
    ArrivingAt = models.CharField(max_length=50)
    ArrivalAirportandTerminal = models.CharField(max_length=50)
    Barcode = models.CharField(max_length=50)
    TicketValidity = models.CharField(max_length=50)


# Hotels
class HOTELBOOKING(models.Model):
    Id = models.AutoField(primary_key=True)
    HotelName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Travelers = models.CharField(max_length=50)
    Rooms = models.CharField(max_length=50)
    RoomType = models.CharField(max_length=50)
    CheckIn = models.CharField(max_length=50)
    CheckOut = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)
