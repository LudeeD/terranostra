from django.contrib import admin

# Register your models here.
from .models import Profile, Report, ImageUploads, Votes

admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(ImageUploads)
admin.site.register(Votes)
