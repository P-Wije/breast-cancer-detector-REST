from django.shortcuts import render
from rest_framework import generics
from .models import Patient, DiagnosticRecord
from .serializers import PatientSerializer, DiagnosticRecordSerializer


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DiagnosticRecordCreateView(generics.ListCreateAPIView):
    queryset = DiagnosticRecord.objects.all()
    serializer_class = DiagnosticRecordSerializer

class DiagnosticRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiagnosticRecord.objects.all()
    serializer_class = DiagnosticRecordSerializer

