from django_filters import rest_framework as filters

from core.apps.accounts.models import ManagerModel


class ManagerFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ManagerModel
        fields = [
            "name",
        ]
