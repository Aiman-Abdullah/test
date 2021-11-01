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

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from home_page import views
# from my_django_app import views as views2



 




urlpatterns = [

    url('^$', views.homePage, name = 'index'),
    url('contact_us', views.contact_us, name = 'contact_us'),
    url('contact_us_2', views.contact_us_2, name = 'contact_us_2'),
    url('contact_us_submitted', views.contact_us_submitted, name = 'contact_us_submitted'),
    # url('^$', views.homePage, name = 'home_page'),

]                            
 