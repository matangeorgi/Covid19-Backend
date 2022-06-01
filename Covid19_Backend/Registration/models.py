from django.db import models

# Create your models here.

class CitizenDetails(models.Model):
    CitizenId = models.AutoField(primary_key=True)
    CitizenFirstName = models.CharField(max_length=50)
    CitizenLastName = models.CharField(max_length=50)
    CitizenDOB = models.DateField()
    CitizenAddress = models.CharField(max_length=100)
    CitizenCity = models.CharField(max_length=50)
    CitizenZipCode = models.IntegerField(null=True, blank=True)
    CitizenCellular = models.IntegerField()
    CitizenLandLine = models.CharField(max_length=50)
    CitizenInfected = models.BooleanField()
    CitizenConditions = models.CharField(max_length=100, blank=True)


    
