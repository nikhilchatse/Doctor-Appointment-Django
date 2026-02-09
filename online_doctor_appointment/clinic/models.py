from django.db import models
from django.conf import settings
# Create your models here.


class DoctorProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='doctor_profile')
    department=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=GENDER_CHOICES,default='M')
    consultation_fees = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    availability = models.CharField(max_length=50, default="Mon-Fri, 10am-5pm")

    def __str__(self):
        return f'Dr. {self.user.username}-{self.department}'
    

class PatientProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='patient_profile')
    gender=models.CharField(max_length=50,choices=GENDER_CHOICES)
    age=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=10,blank=True)
    medical_history=models.TextField(blank=True)

    def __str__(self):
        return f'patient {self.user.username}'
    
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE,related_name="doctor_as_appointment")
    patient=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="patient_as_appointment")

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    symptoms = models.TextField()
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    refer_by=models.ForeignKey(DoctorProfile,on_delete=models.SET_NULL,null=True,blank=True,related_name='refer_made')

    def __str__(self):
        return f"Appt: {self.patient.username} with {self.doctor}"