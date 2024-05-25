from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import PatientListCreateView, PatientDetailView

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<str:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
