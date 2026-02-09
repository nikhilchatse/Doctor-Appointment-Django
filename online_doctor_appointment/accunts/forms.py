from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class PatientSignupForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    class Meta:
        model=User
        fields=['username','email','address','profile_photo']

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })