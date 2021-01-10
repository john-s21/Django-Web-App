from django import forms
from .models import Reg


class AccRegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ["f_name", "l_name", "usr_name", "mail"]
