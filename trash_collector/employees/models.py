from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories


class Employee(models.Model):
    name = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)