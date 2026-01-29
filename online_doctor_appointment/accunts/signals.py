
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from clinic.models import DoctorProfile, PatientProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       
        if instance.role == 'doctor':
            DoctorProfile.objects.create(user=instance)
        
        
        elif instance.role == 'patient':
            PatientProfile.objects.create(user=instance)