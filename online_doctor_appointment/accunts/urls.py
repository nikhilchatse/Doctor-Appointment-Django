from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.patient_signup, name='patient_signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard')
]