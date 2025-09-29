from django import forms

from core.apps.accounts.models import DirectorModel


class DirectorForm(forms.ModelForm):

    class Meta:
        model = DirectorModel
        fields = "__all__"
