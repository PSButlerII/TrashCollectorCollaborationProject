from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    employee_zip_code = models.CharField(max_length=5)