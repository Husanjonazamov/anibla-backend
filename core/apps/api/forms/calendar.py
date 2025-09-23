from django import forms

from core.apps.api.models import CalendareventModel


class CalendareventForm(forms.ModelForm):

    class Meta:
        model = CalendareventModel
        fields = "__all__"
