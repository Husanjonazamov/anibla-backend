from rest_framework import serializers

from core.apps.api.models import YearModel


class BaseYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearModel
        fields = [
            "id",
            "name",
        ]


class ListYearSerializer(BaseYearSerializer):
    class Meta(BaseYearSerializer.Meta): ...


class RetrieveYearSerializer(BaseYearSerializer):
    class Meta(BaseYearSerializer.Meta): ...


class CreateYearSerializer(BaseYearSerializer):
    class Meta(BaseYearSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
