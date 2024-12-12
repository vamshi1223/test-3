"""
URL configuration for educationpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from educationapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',views.adminlogin),
    path('contact/',views.contact),
    path('nav/',views.nav),
    path('feedback/',views.feedback),
    path('home/',views.home, name="home"),
    path('admindashboard/',views.admindashboard,name="admindashboard"),
    path('', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('profile_view/', views.profile_view, name='profile_view'),    
    path('students/', views.student_details_view, name='student_details'),
    
]

