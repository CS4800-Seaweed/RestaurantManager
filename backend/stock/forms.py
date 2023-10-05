from django import forms
from .models import RestockRecord

class RestockForm(forms.ModelForm):
    class Meta:
        model = RestockRecord
        fields = ['ingredient', 'added_quantity']
