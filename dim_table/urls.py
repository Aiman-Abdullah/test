
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from dim_table import views 


 
urlpatterns = [
    path('dim_table_upload/', views.simple_upload),

]
 