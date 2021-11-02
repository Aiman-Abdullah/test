
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from jcwf_report_credit_analysis import views 
from jcwf_data_center import views as jcwf_data_center_views

from .dash_apps.finished_apps import jcwf_report_credit_analysis_datatable 

#app_name = ''

urlpatterns = [
    url('jcwf_data_center/list/', jcwf_data_center_views.employee_list, name='jcwf_data_center'),
    path('jcwf_report_credit_analysis/', views.simple_upload, name='jcwf_report_credit_analysis'),
    #path('employee/', jcwf_data_center_views.employee_list, name='jcwf_data_center'),
    #path('employee/', include('jcwf_data_center.urls')),
]
 