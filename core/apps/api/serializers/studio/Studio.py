from rest_framework import serializers

from core.apps.api.models import StudioModel


class BaseStudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudioModel
        fields = [
            "id",
            "name",
        ]


class ListStudioSerializer(BaseStudioSerializer):
    class Meta(BaseStudioSerializer.Meta): ...


class RetrieveStudioSerializer(BaseStudioSerializer):
    class Meta(BaseStudioSerializer.Meta): ...


class CreateStudioSerializer(BaseStudioSerializer):
    class Meta(BaseStudioSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
