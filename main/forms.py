from main.models import PostForm
from django import forms
 
class PostFormForm(forms.ModelForm):
    class Meta:
        model = PostForm