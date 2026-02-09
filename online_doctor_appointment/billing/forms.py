
from django import forms

class MockPaymentForm(forms.Form):
    card_number = forms.CharField(
        max_length=19, 
        label="Card Number", 
        widget=forms.TextInput(attrs={
            'placeholder': '0000 0000 0000 0000', 
            'class': 'form-control',
            'required': 'true'
        })
    )
    expiry_date = forms.CharField(
        max_length=5, 
        label="Expiry Date (MM/YY)", 
        widget=forms.TextInput(attrs={
            'placeholder': '12/25', 
            'class': 'form-control',
            'required': 'true'
        })
    )
    cvv = forms.CharField(
        max_length=3, 
        label="CVV", 
        widget=forms.PasswordInput(attrs={
            'placeholder': '123', 
            'class': 'form-control',
            'required': 'true'
        })
    )
    card_holder = forms.CharField(
        max_length=50, 
        label="Card Holder Name", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Nikhil Chatse', 
            'class': 'form-control',
            'required': 'true'
        })
    )