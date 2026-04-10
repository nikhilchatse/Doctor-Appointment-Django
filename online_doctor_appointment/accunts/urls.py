from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.patient_signup, name='patient_signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # 1. Change Password (while logged in)
    path('password-change/', 
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
         name='password_change'),
    path('password-change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),

    # 2. Reset Password (forgot password)
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), 
         name='password_reset'),

    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
         name='password_reset_confirm'),
         
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
         name='password_reset_complete'),
] 