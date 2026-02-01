from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DoctorProfile,PatientProfile
from .forms import AppointmentForm

# Create your views here.


def doctor_list(request):
    doctors= DoctorProfile.objects.all()

    return render(request,'clinic/doctor_list.html',{'doctors':doctors})

def book_appointment(request,doctor_id):
    doctor=get_object_or_404(DoctorProfile,id=doctor_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)

            appointment.patient = request.user
            appointment.doctor = doctor

            appointment.save()

            messages.info(request,"Appointment Request Send ")
            return redirect('dashboard')
        
    else:
        form = AppointmentForm()
    return render(request,'clinic/book_appointment.html',{'form':form ,'doctor':doctor})