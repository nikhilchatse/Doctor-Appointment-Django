from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientSignupForm
from django.contrib import messages

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
            return redirect('dashboard') # We will create this later
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