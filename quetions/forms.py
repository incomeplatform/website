from django import forms
from .models import SubjectChapterForm

class SelectSubjectChapterForm(forms.Form):
    group = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    board_question = forms.CharField(max_length=100, required=False)
    chapter = forms.CharField(max_length=100, required=False)
