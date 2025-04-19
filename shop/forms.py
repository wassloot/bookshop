from django import forms
from .models import Tea

class TeaForm(forms.ModelForm):
    class Meta:
        model = Tea
        fields = ['name', 'description', 'price', 'origin', 'in_stock']
