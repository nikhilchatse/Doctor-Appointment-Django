from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DoctorProfile,PatientProfile,Appointment
from .forms import AppointmentForm,ReferForm,UserUpdateForm,DoctorProfileForm,PatientProfileForm
from django.db.models import Q
# Create your views here.


@login_required
def doctor_list(request):
    query = request.GET.get('q', '') 
    
    doctors = DoctorProfile.objects.all()
    

    if query:
        doctors = doctors.filter(
            Q(user__first_name__icontains=query) | 
            Q(user__last_name__icontains=query) |
            Q(department__icontains=query) |
            Q(specialization__icontains=query)
        )
        
    return render(request, 'clinic/doctor_list.html', {'doctors': doctors, 'query': query})

@login_required
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

@login_required
def update_appointment(request,appointment_id,new_status):
    appt = get_object_or_404(Appointment,id=appointment_id)

    if request.user.role != 'DOCTOR' or appt.doctor != request.user.doctor_profile:
        messages.error(request, "You are not authorized to manage this appointment.")
        return redirect('dashboard')
    
    appt.status=new_status
    appt.save()

    messages.success(request, f"Appointment marked as {new_status}.")
    return redirect('dashboard')

@login_required
def refer_patient(request,appointment_id):
    current_appt=get_object_or_404(Appointment,id=appointment_id)

    if request.method == 'POST':
        form = ReferForm(request.POST)
        if form.is_valid():
            target_doctor= form.cleaned_data['doctor']
            reason=form.cleaned_data['reason']
            Appointment.objects.create(
                patient=current_appt.patient,
                doctor=target_doctor,
                appointment_date=current_appt.appointment_date,
                appointment_time=current_appt.appointment_time,
                symptoms=f"Refer by Dr.{request.user.last_name}:{reason}",
                status='pending',
                refer_by=current_appt.doctor
            )

            messages.success(request,"Refered Successfully")
            return redirect('dashboard')
    else:
        form = ReferForm()

    return render(request,'clinic/refer_form.html',{'form':form,'appt':current_appt})


#profile edit

@login_required
def edit_profile(request):
    user = request.user
    
    user_form = UserUpdateForm(instance=user)
    
    profile_form = None
    
    if user.role == 'DOCTOR':
        
        profile_form = DoctorProfileForm(instance=user.doctor_profile)
        
    elif user.role == 'PATIENT':
       
        profile_form = PatientProfileForm(instance=user.patient_profile)

    if request.method == 'POST':
        
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        
        if user.role == 'DOCTOR':
            profile_form = DoctorProfileForm(request.POST, instance=user.doctor_profile)
        elif user.role == 'PATIENT':
            profile_form = PatientProfileForm(request.POST, instance=user.patient_profile)

      
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard')
        
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
