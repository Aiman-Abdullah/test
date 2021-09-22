
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from dim_discount import views 
from jcwf_data_center import views as jcwf_data_center_views

from .dash_apps.finished_apps import dim_discount_datatable 

#app_name = ''

urlpatterns = [
    url('employee/', jcwf_data_center_views.employee_list, name='jcwf_data_center'),
    path('dim_discount_upload/', views.simple_upload),
    #path('employee/', jcwf_data_center_views.employee_list, name='jcwf_data_center'),
    #path('employee/', include('jcwf_data_center.urls')),

]
 