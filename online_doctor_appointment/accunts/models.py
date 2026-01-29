from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLE_CHOISE=[
        ('ADMIN','Admin'),
        ('DOCTOR','Doctor'),
        ('PATIENT','Patient')
    ]
    role=models.CharField(max_length=15,choices=ROLE_CHOISE,default='PATIENT')
    profile_photo=models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    address=models.TextField(blank=True)

    def __str__(self):
        return f'{self.username}-{self.role}'