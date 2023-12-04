from django import forms
from .models import RestockRecord, Supply

class AddForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['supply_name', 'storage_location', 'quantity', 'quantity_units', 'supply_description', 'supply_type', 'resupply', 'restaurant']

class RestockForm(forms.ModelForm):
    class Meta:
        model = RestockRecord
        fields = ['supply', 'added_quantity']

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=500, required=False)

    
