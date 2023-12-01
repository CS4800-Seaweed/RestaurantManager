from django import forms
from .models import RestockRecord

class RestockForm(forms.ModelForm):
    class Meta:
        model = RestockRecord
        fields = ['ingredient', 'added_quantity']

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=500, required=False)
    
