from django.shortcuts import render
from rest_framework import generics

from .filters.patient_filter import PatientFilter
from .models import Patient, DiagnosticRecord
from .serializers import PatientSerializer, DiagnosticRecordSerializer
from rest_framework import generics
from .models import Patient
from django_filters import rest_framework as filters


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PatientFilter


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DiagnosticRecordCreateView(generics.ListCreateAPIView):
    queryset = DiagnosticRecord.objects.all()
    serializer_class = DiagnosticRecordSerializer

class DiagnosticRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiagnosticRecord.objects.all()
    serializer_class = DiagnosticRecordSerializer

