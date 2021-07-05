from django import forms
from .models import Customer


class customer_forms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'customer_address', 'customer_zip_code', 'start_suspension_date', 'end_suspension_date',)


class change_pickup_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'weekly_pickup_day', 'onetime_pickup_date',)