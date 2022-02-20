from django import forms
from .models import Client
 
 
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['cid', 'created', 'updated', 'created_by']


class FundWalletForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2)