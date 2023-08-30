from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['fullname',  'parent', 'staffing']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'staffing': forms.NumberInput(attrs={'class': 'form-control'}),
        }
