from datetime import date

from django.db import models


class Patient(models.Model):
    class Meta:
        app_label = 'main_service'
        db_table = 'patients'

    MARITAL_STATUS_CHOICES = [
        (0, 'Single'),
        (1, 'Married'),
        (2, 'Divorced'),
        (3, 'Widowed'),
    ]

    BREAST_PROFILE_CHOICES = [
        (0, 'None'),
        (1, 'Profile 1'),
        (2, 'Profile 2'),
    ]

    id = models.CharField(max_length=255, primary_key=True)
    isNew = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    date = models.DateField(default=date.today)
    dateOfBirth = models.DateField(null=True, blank=True)
    referredBy = models.CharField(max_length=255, blank=True)
    maritalStatus = models.IntegerField(choices=MARITAL_STATUS_CHOICES, default=0)
    breastFeed = models.IntegerField(default=0)
    ageAtFirstPregnancy = models.IntegerField(default=0)
    bcFamilyHistory = models.IntegerField(default=0)
    bcSelfHistory = models.IntegerField(default=0)
    breastProfile = models.IntegerField(choices=BREAST_PROFILE_CHOICES, default=0)
    radiationHistory = models.IntegerField(default=0)
    medConsumptionHistory = models.IntegerField(default=0)
    remarks = models.TextField(blank=True)

    scans = models.JSONField(default=list)
    rois = models.JSONField(default=list)
    anomalies = models.JSONField(default=list)
    edges = models.JSONField(default=list)

    def __str__(self):
        return self.name

