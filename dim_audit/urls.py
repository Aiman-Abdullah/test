
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from dim_product import views 


 
urlpatterns = [
    path('dimProductUpload/', views.simple_upload),

]
 