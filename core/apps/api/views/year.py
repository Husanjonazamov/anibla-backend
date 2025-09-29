from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import YearModel
from core.apps.api.serializers.year import CreateYearSerializer, ListYearSerializer, RetrieveYearSerializer


@extend_schema(tags=["year"])
class YearView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = YearModel.objects.all()
    serializer_class = ListYearSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListYearSerializer,
        "retrieve": RetrieveYearSerializer,
        "create": CreateYearSerializer,
    }
