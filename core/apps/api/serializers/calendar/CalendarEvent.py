from rest_framework import serializers

from core.apps.api.models import CalendareventModel


class BaseCalendareventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendareventModel
        fields = [
            "id",
            "name",
        ]


class ListCalendareventSerializer(BaseCalendareventSerializer):
    class Meta(BaseCalendareventSerializer.Meta): ...


class RetrieveCalendareventSerializer(BaseCalendareventSerializer):
    class Meta(BaseCalendareventSerializer.Meta): ...


class CreateCalendareventSerializer(BaseCalendareventSerializer):
    class Meta(BaseCalendareventSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
