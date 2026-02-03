from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DoctorProfile,PatientProfile,Appointment
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

login_required
def update_appointment(request,appointment_id,new_status):
    appt = get_object_or_404(Appointment,id=appointment_id)

    if request.user.role != 'DOCTOR' or appt.doctor != request.user.doctor_profile:
        messages.error(request, "You are not authorized to manage this appointment.")
        return redirect('dashboard')
    
    appt.status=new_status
    appt.save()

    messages.success(request, f"Appointment marked as {new_status}.")
    return redirect('dashboard')