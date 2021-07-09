from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Customer
from .forms import customer_forms, change_pickup_form
from django.urls import reverse


def index(request):
    user = request.user
    print(user)
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


def customer_validation(request):
    user = request.user
    customer = Customer.objects.filter(user_id=user.id)
    context = {
        'customer': customer,
        'user': user
    }
    return render(request, "customers/base.html", context)


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
    customer = Customer.objects.filter(user_id=user.id).first()
    if customer is None:
        return redirect("/customers/customer")
    customer_info = Customer.objects.get(user_id=user.id)
    form = change_pickup_form(request.POST, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('/customers/')
    context = {
        'form': form,
        'customer': customer
    }
    return render(request, "customers/change_pickup_day.html", context)