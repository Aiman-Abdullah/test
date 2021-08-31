from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_product, Tran_product, Dim_product
from dim_table.models import Dim_table
from .resources import Stage_product_resource, Tran_product_resource, Dim_product_resource

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
        stage_product_resource = Stage_product_resource()
        dataset = Dataset()
        new_stage_products = request.FILES['myfile']
        stage_products = Stage_product.objects.all()
        stage_products.delete()
        imported_data = dataset.load(new_stage_products.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Stage_product(
        		data[0],
        		data[1],
        		data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
        		data[8],
        		)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        # updating transform table

        #         stage_products = Stage_product.objects.filter(product_id='')
        #         stage_products.delete()


        stage_products = Stage_product.objects.all()
        length = Stage_product.objects.count()
        print(str(len(stage_products))+' length of stage products')
        for i in range(0,len(stage_products)):
            
            key = stage_products[i].product_id  
            if Tran_product.objects.filter(product_id=key).exists(): 

                tran_product = Tran_product.objects.filter(product_id=key)

                product_description = Stage_product.objects.get(product_id=key).product_description
                product_pdg = Stage_product.objects.get(product_id=key).product_pdg
                product_type = Stage_product.objects.get(product_id=key).product_type
                product_dtc = Stage_product.objects.get(product_id=key).product_dtc
                product_min_deposit = Stage_product.objects.get(product_id=key).product_min_deposit
                product_phase_out_date = Stage_product.objects.get(product_id=key).product_phase_out_date
                product_disc_date = Stage_product.objects.get(product_id=key).product_disc_date
                if product_disc_date == None:
                    product_discontinued = "N"
                else:
                    product_discontinued = "Y"
                product_col = Stage_product.objects.get(product_id=key).product_col

                row_is_current = "Y"
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "normal update"

                tran_product.update(product_description=product_description, product_pdg=product_pdg, product_type= product_type
                                 , product_dtc =product_dtc , product_min_deposit = product_min_deposit
                                 , product_phase_out_date = product_phase_out_date, product_disc_date = product_disc_date
                                 , product_discontinued =product_discontinued, product_col = product_col


                                 , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

            else:
                product_id = stage_products[i].product_id
                product_description = stage_products[i].product_description
                product_pdg = stage_products[i].product_pdg
                product_type = stage_products[i].product_type
                product_dtc = stage_products[i].product_dtc
                product_min_deposit = stage_products[i].product_min_deposit
                product_phase_out_date = stage_products[i].product_phase_out_date
                
                product_disc_date = stage_products[i].product_disc_date
                if product_disc_date == None:
                    product_discontinued = "N"
                else:
                    product_discontinued = "Y"
                product_col = stage_products[i].product_col


                row_is_current = "Y"
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                tran_product = Tran_product(product_id = product_id, product_description = product_description, product_pdg = product_pdg
                                        , product_type = product_type, product_dtc = product_dtc, product_min_deposit = product_min_deposit
                                        , product_phase_out_date = product_phase_out_date, product_disc_date = product_disc_date, product_col = product_col
                                       
                                       
                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason
                                        )
                tran_product.save()

        print(str(len(stage_products))+' stage_products update successful')
        # loading to datawarehouse tabel
        tran_products = Tran_product.objects.all()
        length = Tran_product.objects.count()

        for i in range(0,len(tran_products)):
            
            key = tran_products[i].product_id  
            if Dim_product.objects.filter(product_id=key).exists(): 

                dim_product = Dim_product.objects.filter(product_id=key)

                product_description = Tran_product.objects.get(product_id=key).product_description
                product_pdg = Tran_product.objects.get(product_id=key).product_pdg
                product_type = Tran_product.objects.get(product_id=key).product_type
                product_dtc = Tran_product.objects.get(product_id=key).product_dtc
                product_min_deposit = Tran_product.objects.get(product_id=key).product_min_deposit
                product_phase_out_date = Tran_product.objects.get(product_id=key).product_phase_out_date
                product_disc_date = Tran_product.objects.get(product_id=key).product_disc_date
                product_discontinued = Tran_product.objects.get(product_id=key).product_discontinued
                product_col = Tran_product.objects.get(product_id=key).product_col

                row_is_current = Tran_product.objects.get(product_id=key).row_is_current
                row_end_date = Tran_product.objects.get(product_id=key).row_end_date
                row_change_reason = "normal update"

                dim_product.update(product_description=product_description, product_pdg=product_pdg, product_type= product_type
                                 , product_dtc =product_dtc , product_min_deposit = product_min_deposit
                                 , product_phase_out_date = product_phase_out_date, product_disc_date = product_disc_date
                                 , product_discontinued = product_discontinued, product_col = product_col

                                 , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)
                #messages.success(request, 'Form successfully submitted') # Any message you wish
            
            else:
                product_id = tran_products[i].product_id
                product_description = tran_products[i].product_description
                product_pdg = tran_products[i].product_pdg
                product_type = tran_products[i].product_type
                product_dtc = tran_products[i].product_dtc
                product_min_deposit = tran_products[i].product_min_deposit
                product_phase_out_date = tran_products[i].product_phase_out_date
                product_disc_date = tran_products[i].product_disc_date
                product_discontinued = tran_products[i].product_discontinued
                product_col = tran_products[i].product_col


                row_is_current = tran_products[i].row_is_current
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                dim_product = Dim_product(product_id = product_id, product_description = product_description, product_pdg = product_pdg
                                        , product_type = product_type, product_dtc = product_dtc, product_min_deposit = product_min_deposit
                                        , product_phase_out_date = product_phase_out_date, product_disc_date = product_disc_date
                                        , product_discontinued = product_discontinued, product_col = product_col


                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason, import_version = 'v 1.0'
                                        , import_batch = 0
                                        , import_user = 'admin'
                                        )
                dim_product.save()
                #messages.success(request, 'Form successfully submitted') # Any message you wish
            from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product")

    number_of_records_imported = Dim_product.objects.count()
    
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block before table is added to dim_table

    tablename = 'test'
    last_import_time = '8/3/2021'
    total_records = 'test'

    # ---------------------------------------------------------------------------------------------------------------------------------------------
     # Use this block after table is added to dim_table
    # last_import_time = Dim_product.objects.extra(order_by = ['row_end_date'])

    # last_import_time = last_import_time[number_of_records_imported-1].row_end_date
    # table = Dim_table.objects.filter(table_name='jcwf_dim_product')
    # table.update(number_of_records_imported=number_of_records_imported, row_end_date=last_import_time
    #            , row_change_reason = 'normal update')
    # tablename = Dim_table.objects.get(table_name='jcwf_dim_product').table_name
    # last_import_time = Dim_table.objects.get(table_name='jcwf_dim_product').row_end_date 
    # total_records = Dim_table.objects.get(table_name='jcwf_dim_product').number_of_records_imported 

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    dim_products_df = Dim_product.objects.all()
    dim_products_df = read_frame(dim_products_df)
    product_names = dim_products_df['product_description'].values.tolist()
    product_ids = dim_products_df['product_id'].values.tolist()
    
    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'product_names':product_names, 'product_ids':product_ids}
             

    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_product")
    return render(request, 'dim_product_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

