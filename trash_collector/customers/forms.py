from django.forms import ModelForm
from .models import Customer



class customer_forms(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'customer_address', 'customer_zip_code', 'start_suspension_date', 'end_suspension_date',)


class change_pickup_form(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'weekly_pickup_day', 'onetime_pickup_date',)


class OneTimePick(ModelForm):
    class Meta:
        model = Customer


class suspend_customer_account(ModelForm):
    class Meta:
        model = Customer



class account_info(ModelForm):
    class Meta:
        model = Customer


class AccountSuspension(ModelForm):
    class Meta:
        model = Customer

