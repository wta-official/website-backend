from django_filters import FilterSet, CharFilter
from django.contrib.postgres.fields import ArrayField
from django.db import models
from .models import Talent
from django_filters import BaseCSVFilter

class TalentFilter(FilterSet):
    roles = CharFilter(method='filter_roles')  # Custom filter for ArrayField

    class Meta:
        model = Talent
        fields = ['roles', 'eye_color', 'hair']  # Add other filterable fields here
        filter_overrides = {
            ArrayField: {
                'filter_class': CharFilter,  # Use CharFilter for ArrayField
            },
        }

    def filter_roles(self, queryset, name, value):
        """
        Custom filtering for the 'roles' ArrayField to support multiple roles.
        """
        roles = value.split(',')  # Split the comma-separated roles
        for role in roles:
            queryset = queryset.filter(**{f"{name}__contains": [role]})
        return queryset


