from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import StudioModel
from core.apps.api.serializers.studio import CreateStudioSerializer, ListStudioSerializer, RetrieveStudioSerializer


@extend_schema(tags=["Studio"])
class StudioView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = StudioModel.objects.all()
    serializer_class = ListStudioSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListStudioSerializer,
        "retrieve": RetrieveStudioSerializer,
        "create": CreateStudioSerializer,
    }
