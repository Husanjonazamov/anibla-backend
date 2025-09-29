from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import CountryModel
from core.apps.api.serializers.country import CreateCountrySerializer, ListCountrySerializer, RetrieveCountrySerializer


@extend_schema(tags=["country"])
class CountryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = ListCountrySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCountrySerializer,
        "retrieve": RetrieveCountrySerializer,
        "create": CreateCountrySerializer,
    }
