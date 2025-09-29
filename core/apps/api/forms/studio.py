from django import forms

from core.apps.api.models import StudioModel


class StudioForm(forms.ModelForm):

    class Meta:
        model = StudioModel
        fields = "__all__"
