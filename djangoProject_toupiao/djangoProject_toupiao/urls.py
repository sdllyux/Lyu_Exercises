"""djangoProject_toupiao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from poll2 import views

urlpatterns = [
    path('', views.show_subjects, name='index'),
    path('teachers/', views.show_teachers),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', views.get_captcha),
    path('mobile/', views.get_mobile_code),
    path('excel/', views.export_teachers_excel),
    path('pdf/', views.export_pdf),
    path('bar/<str:no>/', views.show_bar),
    path('teachers_data/', views.get_teachers_data),
    path('subjects_data/', views.get_subjects_data),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))
