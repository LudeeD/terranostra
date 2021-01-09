from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.PositiveIntegerField()

class Report(models.Model):
    creation_date = models.DateTimeField('date created')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location_lat = models.DecimalField(max_digits=8, decimal_places=5)
    location_lng = models.DecimalField(max_digits=8, decimal_places=5)
    location_geohash  = models.CharField(max_length=12)
    photo = models.ImageField(upload_to='static/upload')
    value = models.PositiveIntegerField()

class Votes(models.Model):
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

class Event(models.Model):
    creation_date = models.DateTimeField('date created')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location_lat = models.DecimalField(max_digits=8, decimal_places=5)
    location_lng = models.DecimalField(max_digits=8, decimal_places=5)
    location_geohash  = models.CharField(max_length=12)
    reports = models.TextField()

 




