from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.accounts.models import ActorprofileModel
from core.apps.accounts.serializers.actor import (
    CreateActorprofileSerializer,
    ListActorprofileSerializer,
    RetrieveActorprofileSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




@extend_schema(tags=["ActorProfile"])
class ActorprofileView(BaseViewSetMixin, ModelViewSet):
    queryset = ActorprofileModel.objects.all()
    serializer_class = ListActorprofileSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListActorprofileSerializer,
        "retrieve": RetrieveActorprofileSerializer,
        "create": CreateActorprofileSerializer,
    }
    def get_serializer_class(self):
        return self.action_serializer_class.get(self.action, self.serializer_class)

    @action(methods=["POST"], detail=False, url_path="register/actor")
    def register(self, request):
        serializer = CreateActorprofileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  
        return Response(
            {"detail": "Foydalanuvchi yaratildi"},
            status=status.HTTP_201_CREATED,
        )