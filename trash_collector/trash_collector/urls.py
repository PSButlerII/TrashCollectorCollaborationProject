from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # First adding our custom routes from our accounts app's urls.py (for our custom registration)
    path('accounts/', include('accounts.urls')),
    # Then adding django's built in routes (login and logout). Notice there is no login function in accounts/views.py
    path('accounts/', include('django.contrib.auth.urls')),
    # Adding all urls from customer app
    path('customers/', include('customers.urls')),
    # Adding all urls from employees app
    path('employees/', include('employees.urls')),
    # 'home' redirects a user to the appropriate index based on their auth group. Investigate views.py for more info
    path('', views.group_redirect, name='home')
]
