from django.urls import path,include
from . import views

urlpatterns = [
    path('create/<int:appointment_id>',views.create_report,name='create_report'),
    path('view/<int:appointment_id>',views.view_report,name='view_report'),
    path('history/<int:patient_id>/', views.patient_history, name='patient_history'),
]