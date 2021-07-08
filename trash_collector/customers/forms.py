from django.forms import ModelForm
from .models import Customer


class CustomerDetails(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class NewServiceForm(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "user",
                  "address",
                  "zip_code",
                  "start_pickup_day",
                  "weekly_pickup_day"}


class OneTimePickup(ModelForm):
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



