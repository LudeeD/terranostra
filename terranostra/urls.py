"""terranostra URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from events.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile, name='profile'),
    path('uploads/<slug:slug>/', uploadedimage, name="uploadedimage"),
    path('reports/', reports, name="reports"),
    path('report/<int:id>/', detail_report, name="detail_report"),
    path('report/<int:id>/endorse/', endorse_report, name="endorse_report"),
    path('report/<int:id>/reject/', reject_report, name="reject_report"),
    path('report/', create_report, name="create_report"),
    path('map/', map_page, name="map_page"),
    path('events/', events, name="events"),
    path('', reports, name="reports"),
]
