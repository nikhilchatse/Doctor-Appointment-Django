from django.contrib import admin
from django.urls import path,include
from .views import checkout
urlpatterns = [
    path('pay/<int:appointment_id>/',checkout, name='checkout'),
]