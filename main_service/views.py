import os

from PIL import Image
from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters.patient_filter import PatientFilter
from .models import DiagnosticRecord, Patient
from .permissions import IsAuthenticatedOrReadOnly
from .serializers import PatientSerializer, DiagnosticRecordSerializer
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


class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'file': {
                        'type': 'string',
                        'format': 'binary',
                        'description': 'Upload an image file. Supported formats: jpeg, png, gif'
                    }
                },
                'required': ['file']
            }
        },
        responses={201: 'File uploaded successfully'}
    )
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, file.name)

        # Validate that the uploaded file is an image
        try:
            image = Image.open(file)
            image.verify()
        except (IOError, SyntaxError, ValidationError):
            return Response({"error": "Invalid image file"}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return Response({"message": "File uploaded successfully", "file_path": file_path},
                        status=status.HTTP_201_CREATED)
