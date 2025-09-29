from rest_framework import serializers

from core.apps.accounts.models import DirectorModel


class BaseDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields = [
            "id",
            "name",
        ]


class ListDirectorSerializer(BaseDirectorSerializer):
    class Meta(BaseDirectorSerializer.Meta): ...


class RetrieveDirectorSerializer(BaseDirectorSerializer):
    class Meta(BaseDirectorSerializer.Meta): ...


class CreateDirectorSerializer(BaseDirectorSerializer):
    class Meta(BaseDirectorSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
