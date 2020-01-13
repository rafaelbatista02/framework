from django import forms

from dono.models import Dono


class DonoForm(forms.ModelForm):
    class Meta:
        model = Dono
        fields = "__all__"