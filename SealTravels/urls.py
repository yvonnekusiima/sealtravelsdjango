"""SealTravels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sealtravelsapp import views
from sealtravelsapp.views import deleteuser
from django.contrib.auth import views as adminlogin

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.index, name='index'),

    # Administrator
    path('administratorlogin/', views.administratorlogin, name='administratorlogin'),
    path('administratorpage/', views.administratorpage, name='administratorpage'),
    path('administratoractivitylog/', views.administratoractivitylog, name='administratoractivitylog'),
    path('useractivityloga/', views.useractivityloga, name='useractivityloga'),
    path('adduser/', views.adduser, name='adduser'),
    path('edituser/', views.edituser, name='edituser'),
    path('changepassworda/', views.changepassworda, name='changepassworda'),
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('userrecords/', views.userrecords, name='userrecords'),

    # Users
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userpage/', views.userpage, name='userpage'),
    path('useractivitylogu/', views.useractivitylogu, name='useractivitylogu'),
    path('changepasswordu/', views.changepasswordu, name='changepasswordu'),

    # Flights
    path('onewaybookinga/', views.onewaybookinga, name='onewaybookinga'),
    path('onewaybookingu/', views.onewaybookingu, name='onewaybookingu'),
    path('roundtripbookinga/', views.roundtripbookinga, name='roundtripbookinga'),
    path('roundtripbookingu/', views.roundtripbookingu, name='roundtripbookingu'),
    path('flightpayment/', views.flightpayment, name='flightpayment'),
    path('flightticketa/', views.flightticket, name='flightticketa'),
    path('flightticketu/', views.flightticket, name='flightticketu'),
    path('onewayrecordsa/', views.onewayrecordsa, name='onewayrecordsa'),
    path('onewayrecordsu/', views.onewayrecordsu, name='onewayrecordsu'),
    path('roundtriprecordsa/', views.roundtriprecordsa, name='roundtriprecordsa'),
    path('roundtriprecordsu/', views.roundtriprecordsu, name='roundtriprecordsu'),
    path('flightpaymentrecordsa/', views.flightpaymentrecordsa, name='flightpaymentrecordsa'),
    path('flightpaymentrecordsu/', views.flightpaymentrecordsu, name='flightpaymentrecordsu'),
    path('flightticketrecordsa/', views.flightticketrecordsa, name='flightticketrecordsa'),
    path('flightticketrecordsu/', views.flightticketrecordsu, name='flightticketrecordsu'),
    path('editonewaybookinga/', views.editonewaybookinga, name='editonewaybookinga'),
    path('editonewaybookingu/', views.editonewaybookingu, name='editonewaybookingu'),
    path('editroundtripbookinga/', views.editroundtripbookinga, name='editroundtripbookinga'),
    path('editroundtripbookingu/', views.editroundtripbookingu, name='editroundtripbookingu'),

    # Hotels
    path('hotelbookinga/', views.hotelbookinga, name='hotelbookinga'),
    path('hotelbookingu/', views.hotelbookingu, name='hotelbookingu'),
    path('hotelrecordsa/', views.hotelrecordsa, name='hotelrecordsa'),
    path('hotelrecordsu/', views.hotelrecordsu, name='hotelrecordsu'),
    path('edithotelbookinga/', views.edithotelbookinga, name='edithotelbookinga'),
    path('edithotelbookingu/', views.edithotelbookingu, name='edithotelbookingu'),
    path('ekohotela/', views.ekohotela, name='ekohotela'),
    path('ekohotelu/', views.ekohotelu, name='ekohotelu'),
    path('hotelbrusselsa/', views.hotelbrusselsa, name='hotelbrusselsa'),
    path('hotelbrusselsu/', views.hotelbrusselsu, name='hotelbrusselsu'),
    path('kigalimarriotthotela/', views.kigalimarriotthotela, name='kigalimarriotthotela'),
    path('kigalimarriotthotelu/', views.kigalimarriotthotela, name='kigalimarriotthotelu'),
    path('lagoonhotela/', views.lagoonhotela, name='lagoonhotela'),
    path('lagoonhotelu/', views.lagoonhotelu, name='lagoonhotelu'),
    path('mestilhotela/', views.mestilhotela, name='mestilhotela'),
    path('mestilhotelu/', views.mestilhotelu, name='mestilhotelu'),
    path('shangrilahotela/', views.shangrilahotela, name='shangrilahotela'),
    path('shangrilahotelu/', views.shangrilahotelu, name='shangrilahotelu'),
    path('themonarchhotela/', views.themonarchhotela, name='themonarchhotela'),
    path('themonarchhotelu/', views.themonarchhotelu, name='themonarchhotelu'),
    path('theoberoihotela/', views.theoberoihotela, name='theoberoihotela'),
    path('theoberoihotelu/', views.theoberoihotelu, name='theoberoihotelu'),
]
