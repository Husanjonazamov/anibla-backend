from django import forms

from core.apps.api.models import CountryModel


class CountryForm(forms.ModelForm):

    class Meta:
        model = CountryModel
        fields = "__all__"
