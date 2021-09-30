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
from jcwf_data_center import views as jcwf_data_center_views
# from firstUI import views as firstUI_views
from home_page import views as home_page_views
from my_django_app import views as my_django_app_views
from dim_customer import views as dim_customer_views
from dim_date import views as dim_date_views
from dim_discount import views as dim_discount_views
from dim_product import views as dim_product_views
from dim_product_group import views as dim_product_group_views
from dim_table import views as dim_table_views 
from fact_sales_order_item import views as fact_sales_order_item_views 
from plotlyDash import views as plotlyDash_views
from test_page import views as test_page_views

urlpatterns = [
    path('signup/', accounts_views.signup_view),
    path('admin/', admin.site.urls), 
    path('upload/', my_django_app_views.simple_upload),
    path('jcwf_data_center/', jcwf_data_center_views.employee_list),
    path('dim_customer/', dim_customer_views.simple_upload),
    path('dim_date/', dim_date_views.simple_upload),
    path('dim_discount/', dim_discount_views.simple_upload),
    path('dim_product/', dim_product_views.simple_upload),
    path('dim_product_group/', dim_product_group_views.simple_upload),
    path('dim_table/', dim_table_views.simple_upload),
    path('fact_sales_order_item/', fact_sales_order_item_views.simple_upload),
    path('', include("django.contrib.auth.urls")),
    path('login/', accounts_views.login_view),
    path('logout/', accounts_views.login_view),
    path('plotlyDash/', plotlyDash_views.plotlyDash),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    
    url('contact_us', home_page_views.contact_us, name = 'home_page'),
    url('^$', home_page_views.homePage, name = 'home_page'),
    # url('selectCountry', firstUI_views.indiCountryData, name='indiCountryData'),
    url(r'^my_django_app/', include('my_django_app.urls')),
    # url(r'^firstUI/', include('firstUI.urls')),
    url(r'^employee/', include('jcwf_data_center.urls'), name='jcwf_data_center'),
    path('dim_accounts/', include('dim_accounts.urls')),
    path('signup/', include('dim_accounts.urls')),
    path('jcwf_data_center/', include('jcwf_data_center.urls')),
    path('dim_date/', include('dim_date.urls')),
    path('dim_discount/', include('dim_discount.urls')),
    path('dim_color/', include('dim_color.urls')),
    path('dim_customer/', include('dim_customer.urls')),
    path('dim_product/', include('dim_product.urls')),
    path('dim_product_group/', include('dim_product_group.urls')),
    path('dim_table/', include('dim_table.urls')),
    path('fact_sales_order_item/', include('fact_sales_order_item.urls')),
    path('home_page/', include('home_page.urls')),
    path('home_page/', home_page_views.homePage),
    path('test_page/', include('test_page.urls')),
    path('test_page/', test_page_views.testPage),
    path('login/', include('dim_accounts.urls')),
    path('logout/', include('dim_accounts.urls')),
    url(r'session_security/', include('session_security.urls')),
]
