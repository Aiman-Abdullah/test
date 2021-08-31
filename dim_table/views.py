from django.shortcuts import render
from django.shortcuts import render

from .models import Dim_table
from dim_audit.models import dimAudit
from .resources import Dim_table_resource

from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")
def simple_upload(request):
    if request.method == 'POST':

        # updating stage table
        stage_table_resource = Dim_table_resource()
        dataset = Dataset()
        new_stage_tables = request.FILES['myfile']
        dim_tables = Dim_table.objects.all()
        dim_tables.delete()
        imported_data = dataset.load(new_stage_tables.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Dim_table(
        		data[0],
        		data[1],
        		data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
        		data[8],
                data[9],
        		)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
    #table = dimTable.objects.filter(tablename='Table')

    tablename = Dim_table.objects.get(table_name='Product').table_name
    context = {'tablename':tablename}

    return render(request, 'dim_table_input.html', context)
