from datetime import date

from django.db import models


class Patient(models.Model):
    class Meta:
        app_label = 'main_service'
        db_table = 'patients'

    BREAST_PROFILE_CHOICES = [
        ('R', 'Right'),
        ('LS', 'Left Side'),
        ('SS', 'Side to Side'),
        ('OB', 'Oblique')
    ]

    FAMILY_BREAST_CANCER_HISTORY_CHOICES = [
        ('N', 'None'),
        ('CL', 'Close'),
        ('SS', 'Same Side'),
        ('DD', 'Distant Degree'),
        ('MM', 'Multiple Members')
    ]

    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    date = models.DateField(default=date.today)
    dateOfBirth = models.DateField(null=True, blank=True)
    referredBy = models.CharField(max_length=255, blank=True)
    maritalStatus = models.BooleanField(default=False)
    breastFeed = models.BooleanField(default=False)
    ageAtFirstPregnancy = models.IntegerField(default=0)
    bcFamilyHistory = models.CharField(choices=FAMILY_BREAST_CANCER_HISTORY_CHOICES, default='N', max_length=2)
    bcSelfHistory = models.BooleanField(default=False)
    breastProfile = models.CharField(choices=BREAST_PROFILE_CHOICES, default='R', max_length=2)
    radiationHistory = models.IntegerField(default=0)
    medConsumptionHistory = models.BooleanField(default=False)
    remarks = models.TextField(blank=True)

    scans = models.JSONField(default=list)
    rois = models.JSONField(default=list)
    anomalies = models.JSONField(default=list)
    edges = models.JSONField(default=list)

    def __str__(self):
        return self.name

