from django import forms
from .models import Client


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'address', 'email_address']
