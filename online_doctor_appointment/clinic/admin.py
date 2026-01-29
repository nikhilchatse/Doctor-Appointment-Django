from django.contrib import admin
from .models import DoctorProfile,PatientProfile,Appointment
# Register your models here.
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(Appointment)