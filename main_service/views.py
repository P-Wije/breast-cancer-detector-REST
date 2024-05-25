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

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        age = self.request.query_params.get('age')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if age:
            queryset = queryset.filter(age=age)
        return queryset

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DiagnosticRecordCreateView(generics.ListCreateAPIView):
    queryset = DiagnosticRecord.objects.all()
    serializer_class = DiagnosticRecordSerializer

class DiagnosticRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiagnosticRecord.objects.all()
    serializer_class = DiagnosticRecordSerializer

