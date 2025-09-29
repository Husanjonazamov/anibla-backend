from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import ManagerModel
from core.apps.accounts.serializers.manager import (
    CreateManagerSerializer,
    ListManagerSerializer,
    RetrieveManagerSerializer,
)


@extend_schema(tags=["manager"])
class ManagerView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ManagerModel.objects.all()
    serializer_class = ListManagerSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListManagerSerializer,
        "retrieve": RetrieveManagerSerializer,
        "create": CreateManagerSerializer,
    }
