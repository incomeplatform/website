# forms.py
from django import forms

class SubjectForm(forms.Form):
    mcq_subject = forms.CharField(required=False)
    written_subject = forms.CharField(required=False)
    delete_mcq = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    delete_written = forms.IntegerField(widget=forms.HiddenInput(), required=False)
