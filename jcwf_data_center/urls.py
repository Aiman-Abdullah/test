from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

from dim_color import views as dim_color_views
from dim_customer import views as dim_customer_views
from dim_date import views as dim_date_views
from dim_discount import views as dim_discount_views
from dim_product import views as dim_product_views
from dim_product_group import views as dim_product_group_views
from fact_sales_order_item import views as fact_sales_order_item_views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), # get and post req. for display operation 
    path('delete/<int:id>', views.employee_delete, name='employee_delete'), # get and post req. for update operation   
    path('list/', views.employee_list, name='employee_list'), # get and post req. for update operation

    path('form/', views.employee_form, name='employee_insert'), # get and post req. for update operation

    url('dim_color/', dim_color_views.simple_upload, name='dim_color'),
    url('dim_customer/', dim_customer_views.simple_upload, name='dim_customer'),
    url('dim_date/', dim_date_views.simple_upload, name='dim_date'),
    url('dim_discount/', dim_discount_views.simple_upload, name='dim_discount'),
    url('dim_product/', dim_product_views.simple_upload, name='dim_product'),
    url('dim_product_group/', dim_product_group_views.simple_upload, name='dim_product_group'),
    url('fact_sales_order_item/', fact_sales_order_item_views.simple_upload, name='fact_sales_order_item'),
]
