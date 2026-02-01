from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientSignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def patient_signup(request):
    if request.method=='POST':
        form=PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.role='PATIENT'
            user.save()

            login(request, user)
            messages.success(request, f"Signup successful! Welcome. ")
            return redirect('dashboard') 
    else:
        form = PatientSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_user(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard') 
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    user=request.user

    if user.role == 'ADMIN':
        return redirect('/admin/')
    elif user.role == 'DOCTOR':
        return render(request,"accounts/doctor_dashboard.html",{'doctor':user.doctor_profile})
    elif user.role == 'PATIENT':
        return render(request,"accounts/patient_dashboard.html",{'patient':user.patient_profile})
    
    return render(request, 'base.html', {'message': 'Role not assigned'})
    