from django.shortcuts import render

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from django.http import HttpResponse

from sealtravelsapp.models import ADMINISTRATOR
from sealtravelsapp.models import ADMINISTRATORACTIVITYLOG
from sealtravelsapp.models import USERS
from sealtravelsapp.models import USERACTIVITYLOG
from sealtravelsapp.models import ONEWAYFLIGHTS
from sealtravelsapp.models import ROUNDTRIPFLIGHTS
from sealtravelsapp.models import HOTELBOOKING
from sealtravelsapp.models import FLIGHTPAYMENTS
from sealtravelsapp.models import FLIGHTTICKETS


# Create your views here.

# Home
def index(request):
    return render(request, 'index.html')


# Administrator
def administratorlogin(request):
    return render(request, 'Administrator/AdministratorLogin.html')


def administratorpage(request):
    return render(request, 'Administrator/AdministratorPage.html')


def administratoractivitylog(request):
    aal = ADMINISTRATORACTIVITYLOG.objects.all()
    return render(request, 'Administrator/AdministratorActivityLog.html', {'viewaal': aal})


def useractivityloga(request):
    ual = USERACTIVITYLOG.objects.all()
    return render(request, 'Administrator/UserActivityLogA.html', {'viewual': ual})


def adduser(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('username') and request.POST.get('dateadded'):
            addusers = USERS()
            addusers.Email = request.POST.get('email')
            addusers.Username = request.POST.get('username')
            password = get_random_string(5)
            hashedpassword = make_password(password)
            addusers.Password = hashedpassword
            addusers.DateAdded = request.POST.get('dateadded')
            addusers.save()
            subject = 'Login Credentials'
            message = 'Your username is ' + request.POST.get('username') + '\n' + 'Your password is ' + password
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(userrecords)
    else:
        return render(request, 'Administrator/AddUser.html')


def userrecords(request):
    users = USERS.objects.all()
    return render(request, 'Administrator/UserRecords.html', {'viewusers': users})


def edituser(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('username'):
            editusers = USERS.objects.get(Username=request.POST.get('username'))
            editusers.Email = request.POST.get('email')
            editusers.Username = request.POST.get('username')
            editusers.save()
            subject = 'Email Change'
            message = 'Hello ' + request.POST.get('username') + ' Your email has been changed'
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(userrecords)
    else:
        return render(request, 'Administrator/EditUser.html')


def changepassworda(request):
    if request.method == 'POST':
        if request.POST.get('administratorid') and request.POST.get('newpassword'):
            passwordchange = ADMINISTRATOR.objects.get(AdministratorId=request.POST.get('administratorid'))
            passwordchange.AdministratorId = request.POST.get('administratorid')
            passwordchange.Password = request.POST.get('newpassword')
            passwordchange.save()
            aal = ADMINISTRATORACTIVITYLOG()
            aal.AdministratorId = 'admin01'
            aal.DateTimestamp = 'admin01'
            aal.Action = 'Changed Password'
            aal.IPAddress = 'admin01'
            aal.HostName = 'admin01'
            aal.save()
            return redirect(userpage)
        else:
            return render(request, 'Administrator/ChangePasswordA.html')


def deleteuser(request):
    return render(request, 'Administrator/UserRecords.html')


# Users
def userlogin(request):
    return render(request, 'Users/UserLogin.html')


def userpage(request):
    return render(request, 'Users/UserPage.html')


def useractivitylogu(request):
    ual = USERACTIVITYLOG.objects.all()
    return render(request, 'Users/UserActivityLogU.html', {'viewual': ual})


def changepasswordu(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('newpassword'):
            passwordchange = USERS.objects.get(Username=request.POST.get('username'))
            passwordchange.Username = request.POST.get('username')
            passwordchange.Password = request.POST.get('newpassword')
            passwordchange.save()
            return redirect(userpage)
        else:
            return render(request, 'Users/ChangePasswordU.html')


# Flights
def onewaybookinga(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            onewaybooking = ONEWAYFLIGHTS()
            onewaybooking.Name = request.POST.get('name')
            onewaybooking.Email = request.POST.get('email')
            onewaybooking.LeavingFrom = request.POST.get('leavingfrom')
            onewaybooking.GoingTo = request.POST.get('goingto')
            onewaybooking.Departing = request.POST.get('departing')
            onewaybooking.Adults = request.POST.get('adults')
            onewaybooking.Children = request.POST.get('children')
            onewaybooking.TripType = request.POST.get('triptype')
            onewaybooking.FlightType = request.POST.get('flighttype')
            onewaybooking.TravelClass = request.POST.get('travelclass')
            onewaybooking.Airline = request.POST.get('airline')
            onewaybooking.Amount = request.POST.get('amount')
            onewaybooking.save()
            subject = 'Flight Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your flight booking has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Leaving From - ' + request.POST.get('leavingfrom') + '\n' + 'Going To - ' + request.POST.get('goingto') + '\n' + 'Departing - ' + request.POST.get('departing') + '\n' + 'Adults - ' + request.POST.get('adults') + '\n' + 'Children - ' + request.POST.get('children') + '\n' + 'Trip Type - ' + request.POST.get('triptype') + '\n' + 'Travel Class - ' + request.POST.get('travelclass') + '\n' + 'Airline - ' + request.POST.get('airline') + '\n' + 'Amount - ' + request.POST.get('amount')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(onewayrecordsa)
    else:
        return render(request, 'Flights/OnewayBookingA.html')


def onewaybookingu(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            onewaybooking = ONEWAYFLIGHTS()
            onewaybooking.Name = request.POST.get('name')
            onewaybooking.Email = request.POST.get('email')
            onewaybooking.LeavingFrom = request.POST.get('leavingfrom')
            onewaybooking.GoingTo = request.POST.get('goingto')
            onewaybooking.Departing = request.POST.get('departing')
            onewaybooking.Adults = request.POST.get('adults')
            onewaybooking.Children = request.POST.get('children')
            onewaybooking.TripType = request.POST.get('triptype')
            onewaybooking.FlightType = request.POST.get('flighttype')
            onewaybooking.TravelClass = request.POST.get('travelclass')
            onewaybooking.Airline = request.POST.get('airline')
            onewaybooking.Amount = request.POST.get('amount')
            onewaybooking.save()
            subject = 'Flight Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your flight booking has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Leaving From - ' + request.POST.get('leavingfrom') + '\n' + 'Going To - ' + request.POST.get('goingto') + '\n' + 'Departing - ' + request.POST.get('departing') + '\n' + 'Adults - ' + request.POST.get('adults') + '\n' + 'Children - ' + request.POST.get('children') + '\n' + 'Trip Type - ' + request.POST.get('triptype') + '\n' + 'Travel Class - ' + request.POST.get('travelclass') + '\n' + 'Airline - ' + request.POST.get('airline') + '\n' + 'Amount - ' + request.POST.get('amount')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(onewayrecordsu)
    else:
        return render(request, 'Flights/OnewayBookingU.html')


def roundtripbookinga(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('returning') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            roundtripbooking = ROUNDTRIPFLIGHTS()
            roundtripbooking.Name = request.POST.get('name')
            roundtripbooking.Email = request.POST.get('email')
            roundtripbooking.LeavingFrom = request.POST.get('leavingfrom')
            roundtripbooking.GoingTo = request.POST.get('goingto')
            roundtripbooking.Departing = request.POST.get('departing')
            roundtripbooking.Departing = request.POST.get('returning')
            roundtripbooking.Adults = request.POST.get('adults')
            roundtripbooking.Children = request.POST.get('children')
            roundtripbooking.TripType = request.POST.get('triptype')
            roundtripbooking.FlightType = request.POST.get('flighttype')
            roundtripbooking.TravelClass = request.POST.get('travelclass')
            roundtripbooking.Airline = request.POST.get('airline')
            roundtripbooking.Amount = request.POST.get('amount')
            roundtripbooking.save()
            subject = 'Flight Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your flight booking has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Leaving From - ' + request.POST.get('leavingfrom') + '\n' + 'Going To - ' + request.POST.get('goingto') + '\n' + 'Departing - ' + request.POST.get('departing') + '\n' + 'Returning - ' + request.POST.get('returning') + '\n' + 'Adults - ' + request.POST.get('adults') + '\n' + 'Children - ' + request.POST.get('children') + '\n' + 'Trip Type - ' + request.POST.get('triptype') + '\n' + 'Travel Class - ' + request.POST.get('travelclass') + '\n' + 'Airline - ' + request.POST.get('airline') + '\n' + 'Amount - ' + request.POST.get('amount')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(roundtriprecordsa)
    else:
        return render(request, 'Flights/RoundtripBookingA.html')


def roundtripbookingu(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('returning') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            roundtripbooking = ROUNDTRIPFLIGHTS()
            roundtripbooking.Name = request.POST.get('name')
            roundtripbooking.Email = request.POST.get('email')
            roundtripbooking.LeavingFrom = request.POST.get('leavingfrom')
            roundtripbooking.GoingTo = request.POST.get('goingto')
            roundtripbooking.Departing = request.POST.get('departing')
            roundtripbooking.Departing = request.POST.get('returning')
            roundtripbooking.Adults = request.POST.get('adults')
            roundtripbooking.Children = request.POST.get('children')
            roundtripbooking.TripType = request.POST.get('triptype')
            roundtripbooking.FlightType = request.POST.get('flighttype')
            roundtripbooking.TravelClass = request.POST.get('travelclass')
            roundtripbooking.Airline = request.POST.get('airline')
            roundtripbooking.Amount = request.POST.get('amount')
            roundtripbooking.save()
            subject = 'Flight Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your flight booking has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Leaving From - ' + request.POST.get('leavingfrom') + '\n' + 'Going To - ' + request.POST.get('goingto') + '\n' + 'Departing - ' + request.POST.get('departing') + '\n' + 'Returning - ' + request.POST.get('returning') + '\n' + 'Adults - ' + request.POST.get('adults') + '\n' + 'Children - ' + request.POST.get('children') + '\n' + 'Trip Type - ' + request.POST.get('triptype') + '\n' + 'Travel Class - ' + request.POST.get('travelclass') + '\n' + 'Airline - ' + request.POST.get('airline') + '\n' + 'Amount - ' + request.POST.get('amount')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(roundtriprecordsu)
    else:
        return render(request, 'Flights/RoundtripBookingU.html')


def flightpayment(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('paymentmethod') and request.POST.get('cardnumber') and request.POST.get('cvv') and request.POST.get('expirydate') and request.POST.get('amount'):
            flightpayments = FLIGHTPAYMENTS()
            flightpayments.Name = request.POST.get('name')
            flightpayments.Email = request.POST.get('email')
            flightpayments.PaymentMethod = request.POST.get('paymentmethod')
            flightpayments.CardNumber = make_password(request.POST.get('cardnumber'))
            flightpayments.CVV = make_password(request.POST.get('cvv'))
            flightpayments.ExpiryDate = request.POST.get('expirydate')
            flightpayments.Amount = request.POST.get('amount')
            flightpayments.save()
            subject = 'Flight Payment'
            message = 'Hello ' + request.POST.get('name') + ', Your flight payment has been recieved \n \n' + 'PAYMENT DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Payment Method - ' + request.POST.get('paymentmethod') + '\n' + 'Amount - ' + request.POST.get('amount')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(flightpayment)
    else:
        return render(request, 'Flights/FlightPayment.html')


def flightticketa(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('flightnumber') and request.POST.get('travelclass') and request.POST.get('checkinopens') and request.POST.get('status') and request.POST.get('departure') and request.POST.get('arrival') and request.POST.get('departingfrom') and request.POST.get('departureairport') and request.POST.get('arrivingat') and request.POST.get('arrivalairport') and request.POST.get('barcode') and request.POST.get('ticketvalidity'):
            flighttickets = FLIGHTTICKETS()
            flighttickets.Name = request.POST.get('name')
            flighttickets.FlightNumber = request.POST.get('flightnumber')
            flighttickets.TravelClass = request.POST.get('travelclass')
            flighttickets.CheckinOpens = request.POST.get('checkinopens')
            flighttickets.Status = request.POST.get('status')
            flighttickets.Departure = request.POST.get('departure')
            flighttickets.Arrival = request.POST.get('arrival')
            flighttickets.DepartingFrom = request.POST.get('departingfrom')
            flighttickets.DepartureAirportandTerminal = request.POST.get('departureairport')
            flighttickets.ArrivingAt = request.POST.get('arrivingat')
            flighttickets.ArrivalAirportandTerminal = request.POST.get('arrivalairport')
            flighttickets.Barcode = request.POST.get('barcode')
            flighttickets.TicketValidity = request.POST.get('ticketvalidity')
            flighttickets.save()
            return redirect(flightticketrecordsa)
    else:
        return render(request, 'Flights/FlightTicketA.html')


def flightticket(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('flightnumber') and request.POST.get('travelclass') and request.POST.get('checkinopens') and request.POST.get('status') and request.POST.get('departure') and request.POST.get('arrival') and request.POST.get('departingfrom') and request.POST.get('departureairport') and request.POST.get('arrivingat') and request.POST.get('arrivalairport') and request.POST.get('barcode') and request.POST.get('ticketvalidity'):
            flighttickets = FLIGHTTICKETS()
            flighttickets.Name = request.POST.get('name')
            flighttickets.FlightNumber = request.POST.get('flightnumber')
            flighttickets.TravelClass = request.POST.get('travelclass')
            flighttickets.CheckinOpens = request.POST.get('checkinopens')
            flighttickets.Status = request.POST.get('status')
            flighttickets.Departure = request.POST.get('departure')
            flighttickets.Arrival = request.POST.get('arrival')
            flighttickets.DepartingFrom = request.POST.get('departingfrom')
            flighttickets.DepartureAirportandTerminal = request.POST.get('departureairport')
            flighttickets.ArrivingAt = request.POST.get('arrivingat')
            flighttickets.ArrivalAirportandTerminal = request.POST.get('arrivalairport')
            flighttickets.Barcode = request.POST.get('barcode')
            flighttickets.TicketValidity = request.POST.get('ticketvalidity')
            flighttickets.save()
            return redirect(flightticketrecordsu)
    else:
        return render(request, 'Flights/FlightTicketU.html')


def onewayrecordsa(request):
    onewayflights = ONEWAYFLIGHTS.objects.all()
    return render(request, 'Flights/OnewayRecordsA.html', {'viewonewayflights': onewayflights})


def onewayrecordsu(request):
    onewayflights = ONEWAYFLIGHTS.objects.all()
    return render(request, 'Flights/OnewayRecordsU.html', {'viewonewayflights': onewayflights})


def roundtriprecordsa(request):
    roundtripflights = ROUNDTRIPFLIGHTS.objects.all()
    return render(request, 'Flights/RoundtripRecordsA.html', {'viewroundtripflights': roundtripflights})


def roundtriprecordsu(request):
    roundtripflights = ROUNDTRIPFLIGHTS.objects.all()
    return render(request, 'Flights/RoundtripRecordsU.html', {'viewroundtripflights': roundtripflights})


def flightpaymentrecordsa(request):
    flightpayments = FLIGHTPAYMENTS.objects.all()
    return render(request, 'Flights/FlightPaymentRecordsA.html', {'viewflightpayments': flightpayments})


def flightpaymentrecordsu(request):
    flightpayments = FLIGHTPAYMENTS.objects.all()
    return render(request, 'Flights/FlightPaymentRecordsU.html', {'viewflightpayments': flightpayments})


def flightticketrecordsa(request):
    flighttickets = FLIGHTTICKETS.objects.all()
    return render(request, 'Flights/FlightTicketRecordsA.html', {'viewflighttickets': flighttickets})


def flightticketrecordsu(request):
    flighttickets = FLIGHTTICKETS.objects.all()
    return render(request, 'Flights/FlightPaymentRecordsU.html', {'viewflighttickets': flighttickets})


def editonewaybookinga(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            editonewaybooking = ONEWAYFLIGHTS.objects.get(Name=request.POST.get('name'))
            editonewaybooking.Email = request.POST.get('email')
            editonewaybooking.LeavingFrom = request.POST.get('leavingfrom')
            editonewaybooking.GoingTo = request.POST.get('goingto')
            editonewaybooking.Departing = request.POST.get('departing')
            editonewaybooking.Adults = request.POST.get('adults')
            editonewaybooking.Children = request.POST.get('children')
            editonewaybooking.TripType = request.POST.get('triptype')
            editonewaybooking.FlightType = request.POST.get('flighttype')
            editonewaybooking.TravelClass = request.POST.get('travelclass')
            editonewaybooking.Airline = request.POST.get('airline')
            editonewaybooking.Amount = request.POST.get('amount')
            editonewaybooking.save()
            return redirect(onewayrecordsa)
        else:
            return render(request, 'Flights/EditOnewayBookingA.html')


def editonewaybookingu(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            editonewaybooking = ONEWAYFLIGHTS.objects.get(Name=request.POST.get('name'))
            editonewaybooking.Email = request.POST.get('email')
            editonewaybooking.LeavingFrom = request.POST.get('leavingfrom')
            editonewaybooking.GoingTo = request.POST.get('goingto')
            editonewaybooking.Departing = request.POST.get('departing')
            editonewaybooking.Adults = request.POST.get('adults')
            editonewaybooking.Children = request.POST.get('children')
            editonewaybooking.TripType = request.POST.get('triptype')
            editonewaybooking.FlightType = request.POST.get('flighttype')
            editonewaybooking.TravelClass = request.POST.get('travelclass')
            editonewaybooking.Airline = request.POST.get('airline')
            editonewaybooking.Amount = request.POST.get('amount')
            editonewaybooking.save()
            return redirect(onewayrecordsu)
        else:
            return render(request, 'Flights/EditOnewayBookingU.html')


def editroundtripbookinga(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('returning') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            editroundtripbooking = ROUNDTRIPFLIGHTS.objects.get(Name=request.POST.get('name'))
            editroundtripbooking.Email = request.POST.get('email')
            editroundtripbooking.LeavingFrom = request.POST.get('leavingfrom')
            editroundtripbooking.GoingTo = request.POST.get('goingto')
            editroundtripbooking.Departing = request.POST.get('departing')
            editroundtripbooking.Departing = request.POST.get('returning')
            editroundtripbooking.Adults = request.POST.get('adults')
            editroundtripbooking.Children = request.POST.get('children')
            editroundtripbooking.TripType = request.POST.get('triptype')
            editroundtripbooking.FlightType = request.POST.get('flighttype')
            editroundtripbooking.TravelClass = request.POST.get('travelclass')
            editroundtripbooking.Airline = request.POST.get('airline')
            editroundtripbooking.Amount = request.POST.get('amount')
            editroundtripbooking.save()
            return redirect(roundtriprecordsa)
        else:
            return render(request, 'Flights/EditRoundtripBookingA.html')


def editroundtripbookingu(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('leavingfrom') and request.POST.get('goingto') and request.POST.get('departing') and request.POST.get('returning') and request.POST.get('adults') and request.POST.get('children') and request.POST.get('triptype') and request.POST.get('travelclass') and request.POST.get('airline') and request.POST.get('amount'):
            editroundtripbooking = ROUNDTRIPFLIGHTS.objects.get(Name=request.POST.get('name'))
            editroundtripbooking.Email = request.POST.get('email')
            editroundtripbooking.LeavingFrom = request.POST.get('leavingfrom')
            editroundtripbooking.GoingTo = request.POST.get('goingto')
            editroundtripbooking.Departing = request.POST.get('departing')
            editroundtripbooking.Departing = request.POST.get('returning')
            editroundtripbooking.Adults = request.POST.get('adults')
            editroundtripbooking.Children = request.POST.get('children')
            editroundtripbooking.TripType = request.POST.get('triptype')
            editroundtripbooking.FlightType = request.POST.get('flighttype')
            editroundtripbooking.TravelClass = request.POST.get('travelclass')
            editroundtripbooking.Airline = request.POST.get('airline')
            editroundtripbooking.Amount = request.POST.get('amount')
            editroundtripbooking.save()
            return redirect(roundtriprecordsu)
        else:
            return render(request, 'Flights/EditRoundtripBookingU.html')


# Hotels
def hotelbookinga(request):
    return render(request, 'Hotels/HotelBookingA.html')


def hotelbookingu(request):
    return render(request, 'Hotels/HotelBookingU.html')


def hotelrecordsa(request):
    hotelbookings = HOTELBOOKING.objects.all()
    return render(request, 'Hotels/HotelRecordsA.html', {'viewhotelbookings': hotelbookings})


def hotelrecordsu(request):
    hotelbookings = HOTELBOOKING.objects.all()
    return render(request, 'Hotels/HotelRecordsU.html', {'viewhotelbookings': hotelbookings})


def edithotelbookinga(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            edithotelbooking = HOTELBOOKING.objects.get(Name=request.POST.get('name'))
            edithotelbooking.HotelName = request.POST.get('hotelname')
            edithotelbooking.Name = request.POST.get('name')
            edithotelbooking.Email = request.POST.get('email')
            edithotelbooking.Travelers = request.POST.get('travelers')
            edithotelbooking.Rooms = request.POST.get('rooms')
            edithotelbooking.RoomType = request.POST.get('roomtype')
            edithotelbooking.CheckIn = request.POST.get('checkin')
            edithotelbooking.CheckOut = request.POST.get('checkout')
            edithotelbooking.save()
            return redirect(hotelrecordsa)
        else:
            return render(request, 'Hotels/EditHotelBookingA.html')


def edithotelbookingu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            edithotelbooking = HOTELBOOKING.objects.get(Name=request.POST.get('name'))
            edithotelbooking.HotelName = request.POST.get('hotelname')
            edithotelbooking.Name = request.POST.get('name')
            edithotelbooking.Email = request.POST.get('email')
            edithotelbooking.Travelers = request.POST.get('travelers')
            edithotelbooking.Rooms = request.POST.get('rooms')
            edithotelbooking.RoomType = request.POST.get('roomtype')
            edithotelbooking.CheckIn = request.POST.get('checkin')
            edithotelbooking.CheckOut = request.POST.get('checkout')
            edithotelbooking.save()
            return redirect(hotelrecordsu)
        else:
            return render(request, 'Hotels/EditHotelBookingU.html')


def ekohotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/EkoHotelA.html')


def ekohotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/EkoHotelU.html')


def hotelbrusselsa(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/HotelBrusselsA.html')


def hotelbrusselsu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/HotelBrusselsU.html')


def kigalimarriotthotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/KigaliMarriottHotelA.html')


def kigalimarriotthotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/KigaliMarriottHotelU.html')


def lagoonhotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/LagoonHotelA.html')


def lagoonhotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/LagoonHotelU.html')


def mestilhotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/MestilHotelA.html')


def mestilhotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/MestilHotelU.html')


def shangrilahotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/Shangri-laHotelA.html')


def shangrilahotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/Shangri-laHotelU.html')


def themonarchhotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/TheMonarchHotelA.html')


def themonarchhotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/TheMonarchHotelU.html')


def theoberoihotela(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsa)
    else:
        return render(request, 'Hotels/TheOberoiHotelA.html')


def theoberoihotelu(request):
    if request.method == 'POST':
        if request.POST.get('hotelname') and request.POST.get('name') and request.POST.get('email') and request.POST.get('travelers') and request.POST.get('rooms') and request.POST.get('roomtype') and request.POST.get('checkin') and request.POST.get('checkout'):
            hotelbooking = HOTELBOOKING()
            hotelbooking.HotelName = request.POST.get('hotelname')
            hotelbooking.Name = request.POST.get('name')
            hotelbooking.Email = request.POST.get('email')
            hotelbooking.Travelers = request.POST.get('travelers')
            hotelbooking.Rooms = request.POST.get('rooms')
            hotelbooking.RoomType = request.POST.get('roomtype')
            hotelbooking.CheckIn = request.POST.get('checkin')
            hotelbooking.CheckOut = request.POST.get('checkout')
            hotelbooking.save()
            subject = 'Hotel Booking'
            message = 'Hello ' + request.POST.get('name') + ', Your booking at ' + request.POST.get('hotelname') + ' has been recieved \n \n' + 'BOOKING DETAILS \n' + 'Name - ' + request.POST.get('name') + '\n' + 'Travelers - ' + request.POST.get('travelers') + '\n' + 'Rooms - ' + request.POST.get('rooms') + '\n' + 'Room Type - ' + request.POST.get('roomtype') + '\n' + 'Check-in - ' + request.POST.get('checkin') + '\n' + 'Check-out - ' + request.POST.get('checkout')
            mailfrom = 'Yvonne WorkAccount'
            mailto = [request.POST.get('email')]
            send_mail(subject, message, mailfrom, mailto)
            return redirect(hotelrecordsu)
    else:
        return render(request, 'Hotels/TheOberoiHotelU.html')