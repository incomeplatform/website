# forms.py
from django import forms
from .models import DynamicTable

class DynamicTableForm(forms.ModelForm):
    class Meta:
        model = DynamicTable
        fields = '__all__'
