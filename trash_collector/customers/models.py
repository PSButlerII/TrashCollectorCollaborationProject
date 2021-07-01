from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser, PermissionsMixin
from django.utils.translation import ugettext_lazy
# Create your models here.

#Will use for the 1 to 1 object creation: Will explain with partner!
from django.db.models.signals import post_save
from django.dispatch import receiver


# TODO: Finish customer model by adding necessary properties to fulfill user stories

#Discuss revisions prior to migration or futher updates to database:


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True)
    address = models.TextField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    date_of_subscription = models.DateTimeField(auto_now_add=True)
    weekly_pick_up_day = models.TextField(max_length=50, blank=True)
    active_subscription = models.BooleanField(True)