from django_filters import rest_framework as filters

from core.apps.api.models import AnimeModel


class AnimeFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = AnimeModel
        fields = [
            "name",
        ]
