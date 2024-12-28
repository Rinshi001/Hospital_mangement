from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', views.addD, name='add_department'),
    path('dreg/', views.doctorreg, name='doctor_registration'),
    path('adminH/', views.adminhome, name='admin_home'),
    path('', views.homeH, name='home'),
    path('preg/', views.patientreg, name='patient_registration'),
    path('lgs/', views.loginh, name='login'),
    path('docth/', views.doctorhome, name='doctor_home'),
    path('patient-home/', views.patienthome, name='patient_home'),
    path('lgout/', views.lgout, name='logout'),
    path('updatedr/', views.updateprofiledr, name='update_doctor_profile'),
    path('update-doctor/<int:uid>/', views.update_Doctors, name='update_doctor'),
    path('update-patient/<int:uid>/', views.update_patient, name='update_patient'),
    path('create-booking/', views.create_or_update_booking, name='create_booking'),
    path('update-booking/<int:booking_id>/', views.create_or_update_booking, name='update_booking'),
    path('bookings/', views.list_bookings, name='list_bookings'),
    path('bookings/approve/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('bookings/approved/', views.approved_bookings, name='approved_bookings'),
    path('dview/', views.dview, name='doctor_view'),
    path('bookings/by-doctor/', views.view_bookings_by_doctor, name='admin_bookings_by_doctor'),

    
]
