from django import forms
from .models import Employer


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name',  'position', 'department',
                  'salary', 'work_since', 'birth_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'work_since': forms.DateInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
