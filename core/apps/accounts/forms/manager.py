from django import forms

from core.apps.accounts.models import ManagerModel


class ManagerForm(forms.ModelForm):

    class Meta:
        model = ManagerModel
        fields = "__all__"
