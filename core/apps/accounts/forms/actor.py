from django import forms

from core.apps.accounts.models import ActorprofileModel


class ActorprofileForm(forms.ModelForm):

    class Meta:
        model = ActorprofileModel
        fields = "__all__"
