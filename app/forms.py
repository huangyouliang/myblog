from django import forms
from app.models import *

class CommentForm(forms.ModelForm):
    # username = forms.ModelForm(label='名称',)
    # create_time = forms.DateTimeField()
    # content = forms.Textarea()
    class Meta:
        model = Comment
        fields = ("user","content","article")
        # exclude = ("username",)
