from django.shortcuts import render,redirect,get_object_or_404
from .models import medicalreports
from .forms import reportform
from clinic.models import Appointment
from django.contrib import messages

# Create your views here.

def create_report(request,appointment_id):
    appointment = get_object_or_404(Appointment,id=appointment_id)
    
    if request.user.role != 'DOCTOR' or appointment.doctor != request.user.doctor_profile:
        return redirect('doctor_dashboard')
    
    if request.method == 'POST':
        form = reportform(request.POST,request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.appointment = appointment
            report.save()

            appointment.status='completed'
            appointment.save()

            messages.success(request, "Report sent to patient!")
            return redirect('dashboard')
    else:
        form = reportform()
    return render(request, 'reports/create_report.html', {'form': form, 'appointment': appointment})
    

def view_report(request,appointment_id):
    appointment =get_object_or_404(Appointment,id=appointment_id)

    try:
        report = appointment.modical_report
    except medicalreports.DoesNotExist:
        messages.error(request, "Report not ready yet.")
        return redirect('dashboard')
    
    return render(request, 'reports/view_report.html', {'report': report})