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
        pass


class OneTimePick(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "address",
                  "zip_code",
                  "onetime_pickup"}


class AccountSuspension(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "address",
                  "zip_code",
                  "start_suspension",
                  "end_suspension"}



class account_info(ModelForm):
    class Meta:
        model = Customer
        pass




