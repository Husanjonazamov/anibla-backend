from django import forms

from core.apps.api.models import AnimeModel


class AnimeForm(forms.ModelForm):

    class Meta:
        model = AnimeModel
        fields = "__all__"
