from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewServiceForm, OneTimePickup, AccountSuspension, CustomerDetails
from .models import Customer


def index(request):
    user = request.user
    print(user)
    return render(request, 'customers/index.html')


def detail(request, user_id):
    customer = Customer.objects.get(user_id=user_id)
    form = CustomerDetails(instance=customer)
    if request.method == 'POST':
        form = CustomerDetails(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/detail.html', context)


# allows user to sign up for account
def registration(request):
    form = NewServiceForm()
    if request.method == 'POST':
        form = NewServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form}
    return render(request, "customers/registration.html", context)


def change(request, user_id):
    customer = Customer.objects.get(user_id=user_id)
    form = NewServiceForm(instance=customer)
    if request.method == 'POST':
        form = NewServiceForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/change.html', context)


def pickup(request, user_id):
    customer = Customer.objects.get(user_id=user_id)
    form = OneTimePickup(instance=customer)
    if request.method == 'POST':
        form = OneTimePickup(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/pickup.html', context)


def suspension(request, user_id):
    customer = Customer.objects.get(user_id=user_id)
    form = AccountSuspension(instance=customer)
    if request.method == 'POST':
        if Customer.start_suspension(user_id=user_id, null=True):
            Customer.weekly_pickup_day(user_id=user_id, null=False)
        if Customer.start_suspension(user_id=user_id, null=False):
            Customer.weekly_pickup_day(user_id=user_id, null=True)
        form = AccountSuspension(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/suspension.html', context)


def statement(request, user_id):
    customer = Customer.objects.get(user_id=user_id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/statement.html', context)