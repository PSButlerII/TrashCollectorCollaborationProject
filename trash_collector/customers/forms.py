from django.forms import ModelForm
from .models import Customer
# from durationfield.forms import DurationField as FDurationField


class customer_forms(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'customer_address', 'customer_zip_code', 'start_suspension_date', 'end_suspension_date',)


class change_pickup_form(ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'weekly_pickup_day', 'onetime_pickup_date',)

<<<<<<< HEAD
class OneTimePick(ModelForm):
    pass

class suspend_customer_account(ModelForm):
    pass

class account_info(ModelForm):
    pass

class AccountSuspension(ModelForm):
    pass
=======
# class DurationField(forms.ModelForm)
#     duration = FDurationField()
>>>>>>> 373bf9e18c8a117936a1afdbbe23e66ff66754d4
