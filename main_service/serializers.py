from rest_framework import serializers
from .models import Patient, DiagnosticRecord


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DiagnosticRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticRecord
        fields = '__all__'
