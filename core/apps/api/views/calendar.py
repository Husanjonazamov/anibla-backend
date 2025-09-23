from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import CalendareventModel
from core.apps.api.serializers.calendar import (
    CreateCalendareventSerializer,
    ListCalendareventSerializer,
    RetrieveCalendareventSerializer,
)


@extend_schema(tags=["CalendarEvent"])
class CalendareventView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CalendareventModel.objects.all()
    serializer_class = ListCalendareventSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCalendareventSerializer,
        "retrieve": RetrieveCalendareventSerializer,
        "create": CreateCalendareventSerializer,
    }
