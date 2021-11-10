from django.shortcuts import render, redirect
from django.shortcuts import render

from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime

import pandas as pd
from django_pandas.io import read_frame

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")

def simple_upload(request):
    if request.method == 'POST':
        print('posting')
        # updating stage table

    last_import_time = 'test'
    total_records = 'test'
    product_names = 'test'
    product_ids = 'test'

    context = { 'last_import_time':last_import_time
            , 'total_records':total_records, 'product_names':product_names, 'product_ids':product_ids}
            

    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/jcwf_report_credit_analysis_input")
    return render(request, 'jcwf_report_credit_analysis_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

