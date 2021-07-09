

from django.shortcuts import render, redirect
from django.apps import apps
from .models import Employee
from datetime import date
import calendar


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # if not request.user.groups.filter(name="Employees.").exist():
    #     return render(request, 'index.html')
    # Customer = apps.get_model('customers.Customer')
    # user=request.user
    # try:
    #     employee_information = Employee.objects.get(user_id=user.id)
    #     zip_code = Employee.employee_zip_code
    #     today_num= date.today().weekday()
    #     days = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
    #     today_day = days[today_num]
    #     today_date = date.today()
    #     customers = Customer.objects.filter(customer_zip_code=employee_information.employee_zip_code, )
    #     context = {
    #     'customers': customers}
    #     return render(request, 'employees/index.html', context)
    #     except Employee.DoesNotExist:
    #     return HttpResponseRedirect(reverse('employees:create'))

    user = request.user
    employee_information = Employee.objects.get(user_id=user.id)

    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    curr_date = date.today()
    print(curr_date, "curr_date")

    curr_month = curr_date.month
    print(curr_month, "curr_month")

    current_weekday_string = calendar.day_name[curr_date.weekday()]
    print(current_weekday_string)

    # pulls suspension start date from customer model
    customer_suspension_start_date = Customer.objects.filter(start_suspension_date__contains=date.today())
    print(customer_suspension_start_date, "1")

    # pulls the suspension end date from customer models
    customer_suspension_end_date = Customer.objects.filter(end_suspension_date__contains=date.today())
    print(customer_suspension_end_date, "2")

    customer_in_employees_zip = Customer.objects.filter(customer_zip_code=employee_information.employee_zip_code,
                                                        weekly_pickup_day=current_weekday_string
                                                        )
    customers_with_one_time_pickup = Customer.objects.filter(customer_zip_code=employee_information.employee_zip_code,
                                                             onetime_pickup_date=curr_date
                                                             )
    # filter the pickup day, to make sure they are not in between suspended dates
    Customer.start_suspension_date = True
    context = {'customer_for_today': customer_in_employees_zip,
               'one_time_pickup': customers_with_one_time_pickup,
               'customer_suspension_start_date': customer_suspension_start_date,
               'customer_suspension_end_date': customer_suspension_end_date,
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
