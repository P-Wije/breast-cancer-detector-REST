from django.db import models


class Report(models.Model):
    report_id = models.BigAutoField(primary_key=True)
    record_id = models.ForeignKey('DiagnosticRecord', on_delete=models.CASCADE)
    date = models.DateTimeField()
    path = models.CharField(max_length=255)

    def __str__(self):
        return f"Report {self.report_id} for DiagnosticRecord {self.record_id}"

    class Meta:
        db_table = 'reports'
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
