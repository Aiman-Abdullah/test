from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_color, Tran_color, Dim_color
from dim_table.models import Dim_table
from .resources import Stage_color_resource, Tran_color_resource, Dim_color_resource

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
app_start_time = datetime.now()

@login_required(login_url="/accounts/login/")
def simple_upload(request):

    if request.method == 'POST':

        app_start_time = datetime.now()

        # updating stage table
        stage_color_resource = Stage_color_resource()
        dataset = Dataset()
        new_stage_colors = request.FILES['myfile']
        stage_colors = Stage_color.objects.all()
        stage_colors.delete()
        imported_data = dataset.load(new_stage_colors.read(),format='xlsx') # xlsx

        #print(imported_data) 
        for data in imported_data:
        	print(data[1])
        	value = Stage_color(
                [data[0],data[1],data[2],data[3]]
         	,   data[0]               
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
        	)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        # updating transform table

        # clearing transform table for new data
        tran_colors = Tran_color.objects.all()
        tran_colors.delete()
        
        # if Stage_color.objects.filter(color_temp_key=''): 

        #         stage_color = Stage_color.objects.filter(color_temp_key='')
        #         stage_color.delete()


        stage_colors = Stage_color.objects.all()
        length = Stage_color.objects.count()
        print(str(len(stage_colors))+' length of stage color')

        # for i in range(0,len(stage_colors)-1):
        #     day = stage_colors[i].color_temp_key  
        #     if day == "0000-00-00":
        #         day = "2000-01-01"

        for i in range(0,len(stage_colors)):
  
            key = stage_colors[i].color_temp_key  
            if Tran_color.objects.filter(color_temp_key=key).exists(): 

                tran_color = Tran_color.objects.filter(color_temp_key=key)

                color_table = Stage_color.objects.get(color_temp_key=key).color_table
                color_group = Stage_color.objects.get(color_temp_key=key).color_group
                color_name = Stage_color.objects.get(color_temp_key=key).color_name
                color_description = Stage_color.objects.get(color_temp_key=key).color_description
                color_bo_date = Stage_color.objects.get(color_temp_key=key).color_bo_date
                color_disc_group = Stage_color.objects.get(color_temp_key=key).color_disc_group
                color_formula_group = Stage_color.objects.get(color_temp_key=key).color_formula_group
                color_begin_date = Stage_color.objects.get(color_temp_key=key).color_begin_date
                color_discontinued_date = Stage_color.objects.get(color_temp_key=key).color_discontinued_date
                color_inactive_date = Stage_color.objects.get(color_temp_key=key).color_inactive_date
                color_constants = Stage_color.objects.get(color_temp_key=key).color_constants

                row_is_current = "Y"
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "normal update"

                tran_color.update(color_table=color_table,
                                   color_group=color_group
                                 , color_name= color_name
                                 , color_description = color_description
                                 , color_bo_date = color_bo_date
                                 , color_disc_group = color_disc_group
                                 , color_formula_group = color_formula_group
                                 , color_begin_date = color_begin_date
                                 , color_discontinued_date = color_discontinued_date
                                 , color_inactive_date = color_inactive_date
                                 , color_constants = color_constants

                                 , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

            else:
                color_temp_key = stage_colors[i].color_temp_key
                color_table = stage_colors[i].color_table
                color_group = stage_colors[i].color_group
                color_name = stage_colors[i].color_name
                color_description = stage_colors[i].color_description
                color_bo_date = stage_colors[i].color_bo_date
                color_disc_group = stage_colors[i].color_disc_group
                color_formula_group = stage_colors[i].color_formula_group
                color_begin_date = stage_colors[i].color_begin_date
                color_discontinued_date = stage_colors[i].color_discontinued_date
                color_inactive_date = stage_colors[i].color_inactive_date
                color_constants = stage_colors[i].color_constants

                row_is_current = "Y"
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                tran_color = Tran_color(
                                              color_temp_key=color_temp_key
                                            , color_table=color_table
                                            , color_group= color_group
                                            , color_name = color_name
                                            , color_description = color_description
                                            , color_bo_date = color_bo_date
                                            , color_disc_group = color_disc_group
                                            , color_formula_group = color_formula_group
                                            , color_begin_date = color_begin_date
                                            , color_discontinued_date = color_discontinued_date
                                            , color_inactive_date = color_inactive_date
                                            , color_constants = color_constants

                                            , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                            , row_change_reason = row_change_reason
                                        )
                tran_color.save()

        print(str(len(stage_colors))+' tran_color update successful')
        # loading to datawarehouse tabel
        tran_colors = Tran_color.objects.all()
        length = Tran_color.objects.count()
        print(str(len(tran_colors)) + " colors in transform table")
        for i in range(0,len(tran_colors)):
            
            key = tran_colors[i].color_temp_key  
            if Dim_color.objects.filter(color_unique_key=key).exists(): 

                dim_color = Dim_color.objects.filter(color_unique_key=key)

                color_unique_key = Tran_color.objects.get(color_unique_key=key).color_temp_key
                color_table = Tran_color.objects.get(color_unique_key=key).color_table
                color_group = Tran_color.objects.get(color_unique_key=key).color_group
                color_name = Tran_color.objects.get(color_unique_key=key).color_name
                color_description = Tran_color.objects.get(color_unique_key=key).color_description
                color_bo_date = Tran_color.objects.get(color_unique_key=key).color_bo_date
                color_disc_group = Tran_color.objects.get(color_unique_key=key).color_disc_group
                color_formula_group = Tran_color.objects.get(color_unique_key=key).color_formula_group
                color_begin_date = Tran_color.objects.get(color_unique_key=key).color_begin_date
                color_discontinued_date = Tran_color.objects.get(color_unique_key=key).color_discontinued_date
                color_inactive_date = Tran_color.objects.get(color_unique_key=key).color_inactive_date
                color_constants = Tran_color.objects.get(color_unique_key=key).color_constants
                
                row_is_current = Tran_color.objects.get(color_unique_key=key).row_is_current
                row_end_date = Tran_color.objects.get(color_unique_key=key).row_end_date
                row_change_reason = "normal update"

                dim_color.update(
                                  color_unique_key=color_unique_key
                                , color_table=color_table
                                , color_group= color_group
                                , color_name = color_name
                                , color_description = color_description
                                , color_bo_date = color_bo_date
                                , color_disc_group = color_disc_group
                                , color_formula_group = color_formula_group
                                , color_begin_date = color_begin_date
                                , color_discontinued_date = color_discontinued_date
                                , color_inactive_date = color_inactive_date
                                , color_constants = color_constants
                                
                            
                                , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason
                                , import_version = 'v 1.0', import_batch = 0, import_user = 'admin')

                #messages.success(request, 'Form successfully submitted') # Any message you wish
            
            else:
                color_unique_key = tran_colors[i].color_temp_key
                color_table = tran_colors[i].color_table
                color_group = tran_colors[i].color_group
                color_name = tran_colors[i].color_name
                color_description = tran_colors[i].color_description
                color_bo_date = tran_colors[i].color_bo_date
                color_disc_group = tran_colors[i].color_disc_group
                color_formula_group = tran_colors[i].color_formula_group
                color_begin_date = tran_colors[i].color_begin_date
                color_discontinued_date = tran_colors[i].color_discontinued_date
                color_inactive_date = tran_colors[i].color_inactive_date
                color_constants = tran_colors[i].color_constants
                
                row_is_current = tran_colors[i].row_is_current
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                dim_color = Dim_color(
                                          color_unique_key=color_unique_key
                                        , color_table=color_table
                                        , color_group= color_group
                                        , color_name = color_name
                                        , color_description = color_description
                                        , color_bo_date = color_bo_date
                                        , color_disc_group = color_disc_group
                                        , color_formula_group = color_formula_group
                                        , color_begin_date = color_begin_date
                                        , color_discontinued_date = color_discontinued_date
                                        , color_inactive_date = color_inactive_date
                                        , color_constants = color_constants
                                                                    
                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason, import_version = 'v 1.0'
                                        , import_batch = 0
                                        , import_user = 'admin'
                                        )
                dim_color.save() 
                #messages.success(request, 'Form successfully submitted') # Any message you wish
                #print(str(len(dim_colors))+' dim_color update successful')
            from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product_group") 

    number_of_records_imported = Dim_color.objects.count()
    
    last_import_time = Dim_color.objects.extra(order_by = ['row_end_date'])

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
    #dim_color_df = pd.DataFrame(list(Dim_product.objects.all().values()))
    dim_colors_df = Dim_color.objects.all()
    dim_colors_df = read_frame(dim_colors_df)
    color_names = dim_colors_df['color_name'].values.tolist()
    color_ids = dim_colors_df['color_unique_key'].values.tolist()
    
    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'color_names':color_names, 'color_ids':color_ids}
             
    
    #print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_color")
    return render(request, 'dim_color_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

