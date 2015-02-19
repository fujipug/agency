from main.models import FreeStuff
from django import forms
 
class FreeStuffForm(forms.ModelForm):
    class Meta:
        model = FreeStuff
