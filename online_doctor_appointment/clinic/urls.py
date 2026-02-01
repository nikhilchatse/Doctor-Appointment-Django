from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('doctors/',views.doctor_list, name='doctors'),
    path('book/<int:doctor_id>',views.book_appointment,name='book_appointment'),
]