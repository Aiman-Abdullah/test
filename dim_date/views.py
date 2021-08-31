from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_date, Dim_date
from dim_table.models import Dim_table
from .resources import Stage_date_resource, Dim_date_resource

from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime

import pandas as pd
from django_pandas.io import read_frame

from django.contrib import messages
from datetime import datetime

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")
def simple_upload(request):
    if request.method == 'POST':

        app_start_time = datetime.now()

        # updating stage table
        stage_date_resource = Stage_date_resource()
        dataset = Dataset()
        new_stage_dates = request.FILES['myfile']
        stage_dates = Stage_date.objects.all()
        stage_dates.delete()
        imported_data = dataset.load(new_stage_dates.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Stage_date(
        		data[0]
        	,	data[1]
        	,	data[2]
            ,	data[3]
            ,	data[4]
            ,	data[5]
            ,	data[6]
            ,	data[7]
            ,	data[8]
            ,	data[9]
            ,	data[10]
        	,	data[11]
        	,	data[12]
            ,	data[13]

        	)
        	value.save()       


        print(str(len(stage_dates))+' stage_date update successful')
        # loading to datawarehouse tabel
        dim_dates = Stage_date.objects.all()
        length = Stage_date.objects.count()
        print(str(len(stage_dates)) + " dates in transform table")
        for i in range(0,len(stage_dates)):
            
            key = stage_dates[i].date_date_key  
            if Dim_date.objects.filter(date_date_key=key).exists(): 

                dim_date = Dim_date.objects.filter(date_date_key=key)

                date_date_key = Stage_date.objects.get(date_date_key=key).date_date_key
                date_date_name = Stage_date.objects.get(date_date_key=key).date_date_name
                date_full_date_usa = Stage_date.objects.get(date_date_key=key).date_full_date_usa
                date_day_of_week = Stage_date.objects.get(date_date_key=key).date_day_of_week
                date_day_name = Stage_date.objects.get(date_date_key=key).date_day_name
                date_day_of_month = Stage_date.objects.get(date_date_key=key).date_day_of_month
                date_day_of_year = Stage_date.objects.get(date_date_key=key).date_day_of_year
                date_week_of_year = Stage_date.objects.get(date_date_key=key).date_week_of_year
                date_month_name = Stage_date.objects.get(date_date_key=key).date_month_name
                date_month_of_year = Stage_date.objects.get(date_date_key=key).date_month_of_year
                date_quarter = Stage_date.objects.get(date_date_key=key).date_quarter
                date_quarter_name = Stage_date.objects.get(date_date_key=key).date_quarter_name
                date_year_name = Stage_date.objects.get(date_date_key=key).date_year_name
                date_is_weekday = Stage_date.objects.get(date_date_key=key).date_is_weekday

                row_is_current = "Y"
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "normal update"

                dim_date.update(
                                  date_date_key=date_date_key
                                , date_date_name=date_date_name
                                , date_full_date_usa= date_full_date_usa
                                , date_day_of_week = date_day_of_week
                                , date_day_name = date_day_name
                                , date_day_of_month = date_day_of_month
                                , date_day_of_year = date_day_of_year
                                , date_week_of_year = date_week_of_year
                                , date_month_name = date_month_name
                                , date_month_of_year = date_month_of_year
                                , date_quarter = date_quarter
                                , date_quarter_name = date_quarter_name
                                , date_year_name = date_year_name
                                , date_is_weekday = date_is_weekday

                                , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason
                                , import_version = 'v 1.0', import_batch = 0, import_user = 'admin'
                                )

                #messages.success(request, 'Form successfully submitted') # Any message you wish
            
            else:
                date_date_key = stage_dates[i].date_date_key
                date_date_name = stage_dates[i].date_date_name
                date_full_date_usa = stage_dates[i].date_full_date_usa
                date_day_of_week = stage_dates[i].date_day_of_week
                date_day_name = stage_dates[i].date_day_name
                date_day_of_month = stage_dates[i].date_day_of_month
                date_day_of_year = stage_dates[i].date_day_of_year
                date_week_of_year = stage_dates[i].date_week_of_year
                date_month_name = stage_dates[i].date_month_name
                date_month_of_year = stage_dates[i].date_month_of_year
                date_quarter = stage_dates[i].date_quarter
                date_quarter_name = stage_dates[i].date_quarter_name
                date_year_name = stage_dates[i].date_year_name
                date_is_weekday = stage_dates[i].date_is_weekday


                row_is_current = "Y"
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                dim_date = Dim_date(
                                          date_date_key=date_date_key
                                        , date_date_name=date_date_name
                                        , date_full_date_usa= date_full_date_usa
                                        , date_day_of_week = date_day_of_week
                                        , date_day_name = date_day_name
                                        , date_day_of_month = date_day_of_month
                                        , date_day_of_year = date_day_of_year
                                        , date_week_of_year = date_week_of_year
                                        , date_month_name = date_month_name
                                        , date_month_of_year = date_month_of_year
                                        , date_quarter = date_quarter
                                        , date_quarter_name = date_quarter_name
                                        , date_year_name = date_year_name
                                        , date_is_weekday = date_is_weekday

                                                                    
                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason, import_version = 'v 1.0'
                                        , import_batch = 0
                                        , import_user = 'admin'
                                        )
                dim_date.save()
                #messages.success(request, 'Form successfully submitted') # Any message you wish
                print(str(len(dim_dates))+' dim_date update successful')
            from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product_group")

    number_of_records_imported = Dim_date.objects.count()
    
    last_import_time = Dim_date.objects.extra(order_by = ['row_end_date'])

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block after table is added to dim_table

    # last_import_time = last_import_time[number_of_records_imported-1].row_end_date
    # table = Dim_table.objects.filter(table_name='jcwf_dim_product_group')
    # tablename = Dim_table.objects.get(table_name='jcwf_dim_product_group').table_name
    # table.update(number_of_records_imported=number_of_records_imported, row_end_date=last_import_time
    #            , row_change_reason = 'normal update')

    # last_import_time = Dim_table.objects.get(table_name='jcwf_dim_product_group').row_end_date 
    # total_records = Dim_table.objects.get(table_name='jcwf_dim_product_group').number_of_records_imported 

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block before table is added to dim_table

    tablename = 'test'
    last_import_time = '8/3/2021'
    total_records = 'test'

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    #dim_date_df = pd.DataFrame(list(Dim_product.objects.all().values()))
    dim_dates_df = Dim_date.objects.all()
    dim_dates_df = read_frame(dim_dates_df)
    date_names = dim_dates_df['date_date_name'].values.tolist()
    date_ids = dim_dates_df['date_date_key'].values.tolist()
    
    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'date_names':date_names, 'date_ids':date_ids}
             
    
    #print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_date")``
    return render(request, 'dim_date_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

