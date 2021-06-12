from typing import ContextManager
from django import forms

class DocumentForm(forms.Form):
    title       = forms.CharField(max_length=255)
    content     = forms.Textarea(blank=True, null=True)