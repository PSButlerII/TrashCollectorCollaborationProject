from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('employees/', views.employee_signup, name="employee_signup"),
    path('account_info/', views.employee_account_info, name="employee_account_info"),
    path('todays_pickups/', views.todays_pickups, name="todays_pickups"),
    # path('filter/', views.daily_view, name='filter')
]
