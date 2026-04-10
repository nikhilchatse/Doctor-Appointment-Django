from django.shortcuts import render,redirect,get_object_or_404
from .models import medicalreports
from .forms import reportform
from clinic.models import Appointment
from django.contrib import messages
from accunts.models import User
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



def patient_history(request, patient_id):
    # Security check: Ensure only doctors (or admin) can view this
    if request.user.role not in ['DOCTOR', 'ADMIN']:
        messages.error(request, "Access denied.")
        return redirect('dashboard')
        
    patient = get_object_or_404(User, id=patient_id, role='PATIENT')
    
    # Fetch all completed appointments for this patient
    past_appointments = Appointment.objects.filter(
        patient=patient, 
        status='completed'
    ).order_by('-appointment_date')
    
    return render(request, 'reports/patient_history.html', {
        'patient': patient,
        'past_appointments': past_appointments
    })