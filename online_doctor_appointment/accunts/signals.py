
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from clinic.models import DoctorProfile, PatientProfile
from django.contrib.auth import get_user_model
User=get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       
        if instance.role == 'DOCTOR':
            DoctorProfile.objects.create(user=instance)
        
        
        elif instance.role == 'PATIENT':
            PatientProfile.objects.create(user=instance)