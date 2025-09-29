from django import forms

from core.apps.api.models import YearModel


class YearForm(forms.ModelForm):

    class Meta:
        model = YearModel
        fields = "__all__"
