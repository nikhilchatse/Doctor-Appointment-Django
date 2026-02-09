from django import forms
from .models import Appointment
from clinic.models import DoctorProfile


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