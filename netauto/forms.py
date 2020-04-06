from django import forms
from .models import Device

class Scripts(forms.Form):
    script = forms.FileField()


# class Scripts(forms.ModelForm):
#     class Meta:
#         model = Device
#         fields = [
#             'scripts'
#         ]