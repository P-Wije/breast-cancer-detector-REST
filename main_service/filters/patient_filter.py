from django_filters import rest_framework as filters

from main_service.models import Patient


class PatientFilter(filters.FilterSet):
    # Define your filters here
    id = filters.CharFilter(field_name='id')
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')  # returns all matching records
    mobile = filters.CharFilter(field_name="mobile")

    class Meta:
        model = Patient
        fields = ['id', 'name', 'mobile']