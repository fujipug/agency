from main.models import FreeStuff, Candidate
from django import forms
 
class FreeStuffForm(forms.ModelForm):
    class Meta:
        model = FreeStuff

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate