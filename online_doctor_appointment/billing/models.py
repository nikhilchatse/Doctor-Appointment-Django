
from django.db import models
from clinic.models import Appointment

class Payment(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='payment_details')
    transaction_id = models.CharField(max_length=50, unique=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, default='Credit Card')
    is_successful = models.BooleanField(default=True) 

    def __str__(self):
        return f"Payment {self.transaction_id} for {self.appointment}"