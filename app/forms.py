from django import forms
from .models import Department, Employer


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['fullname',  'parent', 'staffing']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'staffing': forms.NumberInput(attrs={'class': 'form-control'}),
        }


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
