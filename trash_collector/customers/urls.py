from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('customer/', views.customer_signup, name="customer_signup"),
    path('account_info/', views.customer_account_info, name="customer_account_info"),
    path('weekly_pickup/<int:customer_id>/', views.change_pickup_day, name="change_pickup_day")
]
