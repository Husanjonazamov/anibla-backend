from rest_framework import serializers

from core.apps.accounts.models import ManagerModel


class BaseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerModel
        fields = [
            "id",
            "name",
        ]


class ListManagerSerializer(BaseManagerSerializer):
    class Meta(BaseManagerSerializer.Meta): ...


class RetrieveManagerSerializer(BaseManagerSerializer):
    class Meta(BaseManagerSerializer.Meta): ...


class CreateManagerSerializer(BaseManagerSerializer):
    class Meta(BaseManagerSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
