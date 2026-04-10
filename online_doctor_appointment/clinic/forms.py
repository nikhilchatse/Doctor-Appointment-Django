from django import forms
from .models import Appointment
from clinic.models import DoctorProfile,PatientProfile
from accunts.models import User


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date','appointment_time','symptoms']

        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'symptoms': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

class ReferForm(forms.Form):
    doctor= forms.ModelChoiceField(
        queryset=DoctorProfile.objects.all(),
        label="Select Doctor",
        widget=forms.Select(attrs={'rows':3,'class':'form-control'})
    )
    reason=forms.CharField(
        widget=forms.Textarea(attrs={'rows':3,'class':'form-control'}),
        label="Reason For Referal"
    )

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_photo', 'address']

# 2. Doctor Specific Form
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['department', 'specialization', 'consultation_fees', 'availability','gender']

# 3. Patient Specific Form
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['age', 'blood_group', 'medical_history','gender']