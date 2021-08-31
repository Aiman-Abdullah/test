from django.urls import path
from . import views
from .dash_apps.finished_apps import simpleexample 



urlpatterns =[
    path('plotlyDash', views.plotlyDash, name = 'plotlyDash')
]
