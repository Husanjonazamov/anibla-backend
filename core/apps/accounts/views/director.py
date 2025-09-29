from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import DirectorModel
from core.apps.accounts.serializers.director import (
    CreateDirectorSerializer,
    ListDirectorSerializer,
    RetrieveDirectorSerializer,
)


@extend_schema(tags=["director"])
class DirectorView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = DirectorModel.objects.all()
    serializer_class = ListDirectorSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDirectorSerializer,
        "retrieve": RetrieveDirectorSerializer,
        "create": CreateDirectorSerializer,
    }
