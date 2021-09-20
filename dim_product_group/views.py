from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_product_group, Tran_product_group, Dim_product_group
from dim_table.models import Dim_table
from .resources import Stage_product_group_resource, Tran_product_group_resource, Dim_product_group_resource

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

        # updating stage table
        stage_product_group_resource = Stage_product_group_resource()
        dataset = Dataset()
        new_stage_product_groups = request.FILES['myfile']
        stage_product_groups = Stage_product_group.objects.all()
        #stage_products.delete()
        imported_data = dataset.load(new_stage_product_groups.read(),format='xlsx')
        
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Stage_product_group(
        		data[0],
        		data[1],
        		data[2],
                data[3],
                data[4],
                data[5],
                data[6],
        		)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        # updating transform table

        if Stage_product_group.objects.filter(product_group=''): 

                stage_product_group = Stage_product_group.objects.filter(product_group='')
                stage_product_group.delete()


        stage_product_groups = Stage_product_group.objects.all()
        length = Stage_product_group.objects.count()

        for i in range(0,len(stage_product_groups)-1):
            
            key = stage_product_groups[i].product_group  
            if Tran_product_group.objects.filter(product_group=key).exists(): 

                tran_product_group = Tran_product_group.objects.filter(product_group=key)

                product_group_description = Stage_product_group.objects.get(product_group=key).product_group_description
                product = Stage_product_group.objects.get(product_group=key).product
                product_description = Stage_product_group.objects.get(product_group=key).product_description
                product_type = Stage_product_group.objects.get(product_group=key).product_type
                dealer = Stage_product_group.objects.get(product_group=key).dealer
                oe = Stage_product_group.objects.get(product_group=key).oe

                row_is_current = "Y"
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "normal update"

                tran_product_group.update(product_group_description=product_group_description, product=product, product_description= product_description
                                 , product_type =product_type , dealer = dealer
                                 , oe = oe

                                 , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

            else:
                product_group = stage_product_groups[i].product_group
                product_group_description = stage_product_groups[i].product_group_description
                product = stage_product_groups[i].product
                product_description = stage_product_groups[i].product_description
                product_type = stage_product_groups[i].product_type
                dealer = stage_product_groups[i].dealer
                oe = stage_product_groups[i].oe

                row_is_current = "Y"
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                tran_product_group = Tran_product_group(product_group = product_group, product_group_description = product_group_description, product = product
                                        , product_description = product_description, product_type = product_type, dealer = dealer
                                        , oe = oe

                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason
                                        )
                tran_product_group.save()

        # loading to datawarehouse tabel
        tran_product_groups = Tran_product_group.objects.all()
        length = Tran_product_group.objects.count()

        for i in range(0,len(tran_product_groups)):
            
            key = tran_product_groups[i].product_group  
            if Dim_product_group.objects.filter(product_group=key).exists(): 

                dim_product_group = Dim_product_group.objects.filter(product_group=key)

                product_group_description = Tran_product_group.objects.get(product_group=key).product_group_description
                product = Tran_product_group.objects.get(product_group=key).product
                product_description = Tran_product_group.objects.get(product_group=key).product_description
                product_type = Tran_product_group.objects.get(product_group=key).product_type
                dealer = Tran_product_group.objects.get(product_group=key).dealer
                oe = Tran_product_group.objects.get(product_group=key).oe

                row_is_current = Tran_product_group.objects.get(product_group=key).row_is_current
                row_end_date = Tran_product_group.objects.get(product_group=key).row_end_date
                row_change_reason = "normal update"

                dim_product_group.update(product_group_description=product_group_description, product=product, product_description= product_description
                                 , product_type =product_type , dealer = dealer
                                 , oe = oe
                                 
                                 , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)
                #messages.success(request, 'Form successfully submitted') # Any message you wish
            
            else:
                product_group = tran_product_groups[i].product_group
                product_group_description = tran_product_groups[i].product_group_description
                product = tran_product_groups[i].product
                product_description = tran_product_groups[i].product_description
                product_type = tran_product_groups[i].product_type
                dealer = tran_product_groups[i].dealer

                row_is_current = tran_product_groups[i].row_is_current
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                dim_product_group = Dim_product_group(product_group = product_group, product_group_description = product_group_description, product = product
                                        , product_description = product_description, product_type = product_type, dealer = dealer
                                        , oe = oe      
                                                                    
                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason, import_version = 'v 1.0'
                                        , import_batch = 0
                                        , import_user = 'admin'
                                        )
                dim_product_group.save()
                #messages.success(request, 'Form successfully submitted') # Any message you wish
            from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product_group")

    number_of_records_imported = Dim_product_group.objects.count()
    
    last_import_time = Dim_product_group.objects.extra(order_by = ['row_end_date'])

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
    #dim_products_df = pd.DataFrame(list(Dim_product.objects.all().values()))
    dim_product_groups_df = Dim_product_group.objects.all()
    dim_product_groups_df = read_frame(dim_product_groups_df)
    product_group_names = dim_product_groups_df['product_group_description'].values.tolist()
    product_group_ids = dim_product_groups_df['product_group'].values.tolist()
    
    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'product_group_names':product_group_names, 'product_group_ids':product_group_ids}
             

    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_product_group")
    return render(request, 'dim_product_group_input.html', context)

# def employee_(request, id):
#     return redirect('/employee/list')

