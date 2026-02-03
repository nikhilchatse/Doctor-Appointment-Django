from django import forms
from .models import medicalreports

class reportform(forms.ModelForm):
    class Meta:
        model=medicalreports
        fields=['diagnosis', 'prescription', 'report_file']

        widgets = {
            'diagnosis': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'prescription': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'report_file': forms.FileInput(attrs={'class': 'form-control'}),
        }