from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import Customer
from .forms import customer_forms, change_pickup_form
from django.urls import reverse


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    return render(request, 'customers/index.html')


def customer_signup(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customer_address = request.POST.get('customer_address')
        customer_zip_code = request.POST.get('customer_zip_code')
        customer_weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_customer = Customer(name=customer_name, customer_address=customer_address, customer_zip_code=customer_zip_code, weekly_pickup_day=customer_weekly_pickup_day, user=request.user)
        new_customer.save()

        return redirect('/customers/')
    else:
        return render(request, 'customers/customer_signup.html')


def customer_account_info(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    form = customer_forms(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/customers/')
    context = {
        'form': form,
        'customer': customer
    }
    return render(request, "customers/account_info.html", context)


def change_pickup_day(request):
    user = request.user
    customer = Customer.objects.get(user_id=user.id)
    form = change_pickup_form(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/customers/')
    context = {
        'form': form,
        'customer': customer
    }
    return render(request, "customers/customer_change_pickup_day.html", context)