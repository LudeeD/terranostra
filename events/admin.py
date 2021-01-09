from django.contrib import admin

# Register your models here.
from .models import Profile, Report, ImageUploads

admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(ImageUploads)
