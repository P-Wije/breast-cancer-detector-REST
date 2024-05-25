from django.db import models

from main_service.models import Patient


class DiagnosticRecord(models.Model):
    record_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, db_column='patient_id')
    date = models.DateTimeField()
    asymmetry = models.IntegerField()
    curvePattern = models.IntegerField()
    hyperthermia = models.IntegerField(null=True, blank=True)
    oneC = models.IntegerField()
    furrow = models.IntegerField()
    pinpoint = models.IntegerField()
    breastProfile = models.IntegerField()
    age = models.IntegerField()
    fUnique = models.IntegerField()
    diagnosticReading = models.IntegerField()

    def __str__(self):
        return f"DiagnosticRecord {self.record_id} for Patient {self.patient_id}"

    class Meta:
        db_table = 'diagnostic_records'
        verbose_name = 'Diagnostic Record'
        verbose_name_plural = 'Diagnostic Records'
