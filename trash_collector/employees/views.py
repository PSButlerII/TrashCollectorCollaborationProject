import form as form
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.apps import apps
from .models import Employee
from datetime import date
import calendar


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    user = request.user
    employee_information = Employee.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    curr_date = date.today()
    print(curr_date)
    current_weekday_string = calendar.day_name[curr_date.weekday()]
    print(current_weekday_string)
    # filter the pickup day, to make sure they are not in between suspended dates



    customer_in_employees_zip = Customer.objects.filter(customer_zip_code=employee_information.employee_zip_code,
                                                        weekly_pickup_day=current_weekday_string
                                                        )
    customers_with_one_time_pickup = Customer.objects.filter(customer_zip_code=employee_information.employee_zip_code,
                                                             onetime_pickup_date=curr_date
                                                             )

    print(customer_in_employees_zip)
    print(employee_information)
    print(customers_with_one_time_pickup)
    context = {
        'customer_for_today': customer_in_employees_zip,
        'one_time_pickup': customers_with_one_time_pickup,

    }
    return render(request, 'employees/index.html', context)


def employee_signup(request):
    if request.method == 'POST':
        employee_name = request.POST.get('name')
        employee_zip_code = request.POST.get('employee_zip_code')
        new_employee = Employee(name=employee_name, employee_zip_code=employee_zip_code, user=request.user)
        new_employee.save()

        return redirect('/employees/')
    else:
        return render(request, 'employees/employee_signup.html')


def employee_account_info(request):
    user = request.user
    employee_info = Employee.objects.filter(user_id=user.id).first
    context = {
        'employee_info': employee_info
    }
    return render(request, 'employees/employee_account_info.html', context)


def todays_pickups(request):
    return render(request, 'employees/todays_pickups.html')
