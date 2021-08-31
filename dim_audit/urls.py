
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from dimProduct import views 


 
urlpatterns = [
    path('dimProductUpload/', views.simple_upload),

]
 