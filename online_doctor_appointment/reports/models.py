from django.db import models
from clinic.models import Appointment
# Create your models here.


class medicalreports(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE,related_name='modical_report')
    diagnosis = models.TextField(help_text="Doctor's findings")
    prescription = models.TextField(help_text="Medicines prescribed")
    report_file=models.FileField(upload_to='reports/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.appointment}"