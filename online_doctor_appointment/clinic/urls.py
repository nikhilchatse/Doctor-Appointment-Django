from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('doctors/',views.doctor_list, name='doctors'),
    path('book/<int:doctor_id>',views.book_appointment,name='book_appointment'),
    path('update_appt/<int:appointment_id>/<str:new_status>',views.update_appointment,name='update_appt'),
    path('refer/<int:appointment_id>/',views.refer_patient,name='refer_patient'),
]