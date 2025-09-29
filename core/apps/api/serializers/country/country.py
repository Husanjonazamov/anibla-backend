from rest_framework import serializers

from core.apps.api.models import CountryModel


class BaseCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = [
            "id",
            "name",
        ]


class ListCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class RetrieveCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class CreateCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta):
        fields = [
            "id",
            "name",
        ]
