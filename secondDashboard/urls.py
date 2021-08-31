"""secondDashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
  
import my_django_app as my_django_app
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from dim_accounts import views as accounts_views 
from employee_register import views as employee_register_views
from firstUI import views as firstUI_views
from my_django_app import views as my_django_app_views
from dim_customer import views as dim_customer_views
from dim_date import views as dim_date_views
from dim_discount import views as dim_discount_views
from dim_product import views as dim_product_views
from dim_product_group import views as dim_product_group_views
from dim_table import views as dim_table_views 
from plotlyDash import views as plotlyDash_views

urlpatterns = [
    path('signup/', accounts_views.signup_view),
    path('admin/', admin.site.urls), 
    path('upload/', my_django_app_views.simple_upload),
    path('employee/', employee_register_views.employee_list),
    path('dim_customer/', dim_customer_views.simple_upload),
    path('dim_date/', dim_date_views.simple_upload),
    path('dim_discount/', dim_discount_views.simple_upload),
    path('dim_product/', dim_product_views.simple_upload),
    path('dim_product_group/', dim_product_group_views.simple_upload),
    path('dim_table/', dim_table_views.simple_upload),
    path('', include("django.contrib.auth.urls")),
    path('login/', accounts_views.login_view),
    path('logout/', accounts_views.login_view),
    path('plotlyDash/', plotlyDash_views.plotlyDash),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    
    url('^$', firstUI_views.indexPage, name = 'index'),
    url('selectCountry', firstUI_views.indiCountryData, name='indiCountryData'),
    url(r'^my_django_app/', include('my_django_app.urls')),
    url(r'^firstUI/', include('firstUI.urls')),
    url(r'^employee/', include('employee_register.urls'), name='employee_register'),
    path('dim_accounts/', include('dim_accounts.urls')),
    path('signup/', include('dim_accounts.urls')),
    path('employee/', include('employee_register.urls')),
    path('dim_date/', include('dim_date.urls')),
    path('dim_discount/', include('dim_discount.urls')),
    path('dim_color/', include('dim_color.urls')),
    path('dim_customer/', include('dim_customer.urls')),
    path('dim_product/', include('dim_product.urls')),
    path('dim_product_group/', include('dim_product_group.urls')),
    path('dim_table/', include('dim_table.urls')),
    path('login/', include('dim_accounts.urls')),
    path('logout/', include('dim_accounts.urls')),
    url(r'session_security/', include('session_security.urls')),
]
