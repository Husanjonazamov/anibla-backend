from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
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
from core.apps.accounts.models.user import User
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.apps.accounts.views.auth import RegisterView





@extend_schema(tags=["ActorProfile"])
class ActorprofileView(BaseViewSetMixin, ModelViewSet):
    queryset = ActorprofileModel.objects.all()
    serializer_class = ListActorprofileSerializer
    permission_classes = [AllowAny]

    
    action_permission_classes = {
        "me": [IsAuthenticated],           
        "register": [AllowAny],         
        "list": [IsAuthenticated],        
        "retrieve": [IsAuthenticated],
    }
    
    action_serializer_class = {
        "list": ListActorprofileSerializer,
        "retrieve": RetrieveActorprofileSerializer,
        "create": CreateActorprofileSerializer,
    }
    def get_serializer_class(self):
        return self.action_serializer_class.get(self.action, self.serializer_class)
    
    def get_permissions(self):
        permission_classes = self.action_permission_classes.get(self.action, self.permission_classes)
        return [perm() for perm in permission_classes]





    @action(methods=["POST"], detail=False, url_path="register")
    def register(self, request):
        user_data = request.data.get("user", {})

        phone = user_data.get("phone")
        if User.objects.filter(phone=phone).exists():
            raise ValidationError({"phone": "Bu telefon raqami bilan foydalanuvchi allaqachon ro'yxatdan o'tgan."})

        register_view = RegisterView()
        user = register_view.create_user(
            phone=user_data.get("phone"),
            username=user_data.get("username"),
            tg_id=user_data.get("tg_id"),
            role="actor", 
            password=user_data.get("password"),
            first_name=user_data.get("first_name", ""),
            last_name=user_data.get("last_name", "")
        )

        user.is_active = True
        user.save()

        serializer = CreateActorprofileSerializer(
            data=request.data,
            context={"user": user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Foydalanuvchi yaratildi"}, status=status.HTTP_201_CREATED)
    
    
    
    
    @action(methods=["GET"], detail=False, url_path="list")
    def actor_list(self, request):
        queryset = self.get_queryset().select_related("user")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=["GET"], detail=False, url_path="me")
    def me(self, request):
        try:
            actor_profile = ActorprofileModel.objects.get(user=request.user)
        except ActorprofileModel.DoesNotExist:
            return Response(
                {"detail": "Sizda aktyor profili mavjud emas."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(actor_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)