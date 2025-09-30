from rest_framework import serializers

from core.apps.accounts.models import ActorprofileModel
from core.apps.accounts.serializers.auth import RegisterSerializer


class BaseActorprofileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = ActorprofileModel
        fields = [
            "id",
            "user",
            "age",
            "bio",
            "avatar"
        ]
        
    def get_user(self, obj):
        from core.apps.accounts.serializers.user import UserSerializer
        return UserSerializer(obj.user).data




class ListActorprofileSerializer(BaseActorprofileSerializer):
    class Meta(BaseActorprofileSerializer.Meta): ...


class RetrieveActorprofileSerializer(BaseActorprofileSerializer):
    class Meta(BaseActorprofileSerializer.Meta): ...
    
class CreateActorprofileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = ActorprofileModel
        fields = [
            "age",
            "gender",
            "bio",
            "avatar"
        ]

    def create(self, validated_data):
        user = self.context.get("user")
        if not user:
            raise serializers.ValidationError("User is required to create actor profile")

        actor = ActorprofileModel.objects.create(user=user, **validated_data)
        return actor


