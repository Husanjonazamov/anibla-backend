from rest_framework import serializers

from core.apps.api.models import AnimeModel


class BaseAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeModel
        fields = [
            "id",
            "name",
        ]


class ListAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...


class RetrieveAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta): ...


class CreateAnimeSerializer(BaseAnimeSerializer):
    class Meta(BaseAnimeSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
