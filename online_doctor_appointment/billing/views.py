from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clinic.models import Appointment
from .models import Payment
from .forms import MockPaymentForm
import uuid
# Create your views here.

@login_required
def checkout(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    fee = appointment.doctor.consultation_fees

    if request.method == 'POST':
        form = MockPaymentForm(request.POST)
        if form.is_valid():
           
            Payment.objects.create(
                appointment=appointment,
                transaction_id=f"TXN-{str(uuid.uuid4())[:8].upper()}", 
                amount=fee,
                is_successful=True
            )
            
            messages.success(request, "Payment Successful! Receipt generated.")
            return redirect('dashboard')
    else:
        form = MockPaymentForm()

    return render(request, 'billing/checkout.html', {
        'form': form, 
        'appointment': appointment, 
        'fee': fee
    })
