from django.contrib import admin

# Register your models here.
from .models import Profile, Report

admin.site.register(Profile)
admin.site.register(Report)
