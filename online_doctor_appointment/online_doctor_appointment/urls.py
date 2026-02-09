"""
URL configuration for online_doctor_appointment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accunts.views import login_user
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accunts.urls')),
    path('clinic/',include('clinic.urls')),
    # path('login',login_user,name='login'),
    path('reports/',include('reports.urls')),
    path('billing/',include('billing.urls')),
    path('',home_view,name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
