from rest_framework import serializers

from core.apps.accounts.models import DirectorModel


class BaseDirectorSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = DirectorModel
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
    

class ListDirectorSerializer(BaseDirectorSerializer):
    class Meta(BaseDirectorSerializer.Meta): ...


class RetrieveDirectorSerializer(BaseDirectorSerializer):
    class Meta(BaseDirectorSerializer.Meta): ...


class CreateDirectorSerializer(BaseDirectorSerializer):
    avatar = serializers.ImageField(required=True, allow_null=True)

    class Meta:
        model = DirectorModel
        
        fields = [
            "age",
            "bio",
            "avatar"
        ]
        
    def create(self, validated_data):
        user = self.context.get("user")
        if not user:
            raise serializers.ValidationError("User is required to create actor profile")
        
        director = DirectorModel.objects.create(user=user, **validated_data)
        return director