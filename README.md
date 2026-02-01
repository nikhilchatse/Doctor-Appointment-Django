Secure Web Application for Online Doctor Appointment System
Use Case Diagram
          





Day 1: Requirement Analysis & Setup
- [x] Project Architecture Designed (SDLC).
- [x] Django Project & Apps created (`accounts`, `clinic`, `billing`, `reports`).
- [x] Git Repo initialized.


Day 2 Checklist
- [x] CustomUser model created in accounts.

- [x] AUTH_USER_MODEL set in settings.py.

- [x] DoctorProfile and PatientProfile created in clinic.

- [x] Appointment model created.

- [x] makemigrations and migrate ran successfully.

Day 3 Checklist
- [x] Added gender field to Models & Migrated.

- [x] Registered models in admin.py.

- [x] Created Superuser (python manage.py createsuperuser).

- [x] Logged into Admin Panel (http://127.0.0.1:8000/admin) and verified tables exist.

- [x] Created signals.py for automation.

- [x] Connected signals in apps.py.

Day 4 Checklist
- [x] Created templates folder & updated settings.py.

- [x] Created base.html with Bootstrap.

- [x] Created PatientSignupForm in forms.py.

- [x] Created signup and login views.

- [x] Created HTML files for Signup and Login.

- [x] Updated URLs.

Day 5 Checklist
- [x] Updated dashboard view in accounts/views.py with logic for Patient vs Doctor.

- [x] Created patient_dashboard.html (displaying dynamic profile data like Age/Blood Group).

- [x] Created doctor_dashboard.html (displaying Department).

- [x] Added LOGIN_REDIRECT_URL in settings.

- [x] Test 1 (Patient): Log in with the patient account


Day 6 Checklist
- [x] Included clinic.urls in the main project urls.py.

- [x] Created AppointmentForm in clinic/forms.py.

- [x] Created doctor_list and book_appointment views.

- [x] Created the HTML templates for listing and booking.