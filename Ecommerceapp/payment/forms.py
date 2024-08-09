from django import forms
from .models import ShippingAdress

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = ['name', 'email', 'adress', 'phone', 'city', 'zip']
        exclude = ['user']
