from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    weekly_pickup_day = models.CharField(max_length=50)
    onetime_pickup_date = models.DateField(null=True, blank=True)
    start_suspension_date = models.DateField(null=True, blank=True)
    end_suspension_date = models.DateField(null=True, blank=True)
    customer_balance = models.IntegerField(default=0)
    customer_address = models.CharField(max_length=50)
    customer_zip_code = models.CharField(max_length=50)
    weekly_pickup_confirmed = True
    suspension = False

