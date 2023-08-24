from django import forms


class DepartmnentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
