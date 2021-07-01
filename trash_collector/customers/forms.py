from django import forms
from .models import Customer


class customer_forms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'customer_address', 'customer_zip_code', 'weekly_pickup_day',)