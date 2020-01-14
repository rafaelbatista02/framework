from django import forms

from gatinho.models import Gatinho


class GatinhoForm(forms.ModelForm):
    class Meta:
        model = Gatinho
        fields = "__all__"




