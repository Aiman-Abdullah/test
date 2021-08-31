from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_discount, Tran_discount, Dim_discount
from dim_table.models import Dim_table
from .resources import Stage_discount_resource, Tran_discount_resource, Dim_discount_resource

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
        stage_discount_resource = Stage_discount_resource()
        dataset = Dataset()
        new_stage_discounts = request.FILES['myfile']
        stage_discounts = Stage_discount.objects.all()
        stage_discounts.delete()
        imported_data = dataset.load(new_stage_discounts.read(),format='xlsx') # xlsx

        #print(imported_data) 
        for data in imported_data:
        	print(data[1])
        	value = Stage_discount(
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
        	)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        # updating transform table

        # clearing transform table for new data
        tran_discounts = Tran_discount.objects.all()
        tran_discounts.delete()
        
        # if Stage_discount.objects.filter(discount_name=''): 

        #         stage_discount = Stage_discount.objects.filter(discount_name='')
        #         stage_discount.delete()


        stage_discounts = Stage_discount.objects.all()
        length = Stage_discount.objects.count()
        print(str(len(stage_discounts))+' length of stage discount')

        # for i in range(0,len(stage_discounts)-1):
        #     day = stage_discounts[i].discount_temp_key  
        #     if day == "0000-00-00":
        #         day = "2000-01-01"

        for i in range(0,len(stage_discounts)):


            
            # key = stage_discounts[i].discount_customer_id  
            key = [str(stage_discounts[i].discount_customer_id) + str(stage_discounts[i].discount_customer_name) 
                 + str(stage_discounts[i].discount_account_type) + str(stage_discounts[i].discount_product_id)
                 + str(stage_discounts[i].discount_product_name) + str(stage_discounts[i].discount_product_discount_category)
                 + str(stage_discounts[i].discount_model) + str(stage_discounts[i].discount_color)
                 ]
            print("key" + str(key))
            if Tran_discount.objects.filter(discount_name=key).exists(): 

                tran_discount = Tran_discount.objects.filter(discount_name=key)

                discount_customer_id = Stage_discount.objects.get(discount_name=key).discount_customer_id
                discount_customer_name = Stage_discount.objects.get(discount_name=key).discount_customer_name
                discount_account_type = Stage_discount.objects.get(discount_name=key).discount_account_type
                discount_product_id = Stage_discount.objects.get(discount_name=key).discount_product_id
                discount_product_name = Stage_discount.objects.get(discount_name=key).discount_product_name
                discount_product_discount_category = Stage_discount.objects.get(discount_name=key).discount_product_discount_category
                discount_model = Stage_discount.objects.get(discount_name=key).discount_model
                discount_color = Stage_discount.objects.get(discount_name=key).discount_color
                discount_discount_group = Stage_discount.objects.get(discount_name=key).discount_discount_group
                discount_discount_from = Stage_discount.objects.get(discount_name=key).discount_discount_from
                discount_discount_to = Stage_discount.objects.get(discount_name=key).discount_discount_to
                discount_eff = Stage_discount.objects.get(discount_name=key).discount_eff
                discount_factor = Stage_discount.objects.get(discount_name=key).discount_factor

                row_is_current = "Y"
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "normal update"

                tran_discount.update(discount_customer_id=discount_customer_id
                                   , discount_customer_name=discount_customer_name
                                   , discount_account_type= discount_account_type
                                   , discount_product_id = discount_product_id
                                   , discount_product_name = discount_product_name
                                   , discount_product_discount_category = discount_product_discount_category
                                   , discount_model = discount_model
                                   , discount_color = discount_color
                                   , discount_discount_group = discount_discount_group
                                   , discount_discount_from = discount_discount_from
                                   , discount_discount_to = discount_discount_to
                                   , discount_eff = discount_eff
                                   , discount_factor = discount_factor

                                   , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

            else:

                discount_name = [str(stage_discounts[i].discount_customer_id) + str(stage_discounts[i].discount_customer_name) 
                     + str(stage_discounts[i].discount_account_type) + str(stage_discounts[i].discount_product_id)
                     + str(stage_discounts[i].discount_product_name) + str(stage_discounts[i].discount_product_discount_category)
                     + str(stage_discounts[i].discount_model) + str(stage_discounts[i].discount_color)]
                print('else key ' + str(discount_name))
                discount_customer_id = stage_discounts[i].discount_customer_id
                discount_customer_name = stage_discounts[i].discount_customer_name
                discount_account_type = stage_discounts[i].discount_account_type
                discount_product_id = stage_discounts[i].discount_product_id
                discount_product_name = stage_discounts[i].discount_product_name
                discount_product_discount_category = stage_discounts[i].discount_product_discount_category
                discount_model = stage_discounts[i].discount_model
                discount_color = stage_discounts[i].discount_color
                discount_discount_group = stage_discounts[i].discount_discount_group
                discount_discount_from = stage_discounts[i].discount_discount_from
                discount_discount_to = stage_discounts[i].discount_discount_to
                discount_eff = stage_discounts[i].discount_eff
                discount_factor = stage_discounts[i].discount_factor

                row_is_current = "Y"
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                tran_discount = Tran_discount(
                                              discount_name = discount_name
                                            , discount_customer_id=discount_customer_id
                                            , discount_customer_name=discount_customer_name
                                            , discount_account_type= discount_account_type
                                            , discount_product_id = discount_product_id
                                            , discount_product_name = discount_product_name
                                            , discount_product_discount_category = discount_product_discount_category
                                            , discount_model = discount_model
                                            , discount_color = discount_color
                                            , discount_discount_group = discount_discount_group
                                            , discount_discount_from = discount_discount_from
                                            , discount_discount_to = discount_discount_to
                                            , discount_eff = discount_eff
                                            , discount_factor = discount_factor

                                            , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                            , row_change_reason = row_change_reason
                                        )
                tran_discount.save()

        print(str(len(tran_discounts))+' tran_discount update successful')
        # loading to datawarehouse tabel
        tran_discounts = Tran_discount.objects.all()
        length = Tran_discount.objects.count()
        print(str(len(tran_discounts)) + " discounts in transform table")
        for i in range(0,len(tran_discounts)):
            
            key = tran_discounts[i].discount_name  
            if Dim_discount.objects.filter(discount_name=key).exists(): 

                dim_discount = Dim_discount.objects.filter(discount_name=key)

                discount_customer_id = Tran_discount.objects.get(discount_name=key).discount_customer_id
                discount_customer_name = Tran_discount.objects.get(discount_name=key).discount_customer_name
                discount_account_type = Tran_discount.objects.get(discount_name=key).discount_account_type
                discount_product_id = Tran_discount.objects.get(discount_name=key).discount_product_id
                discount_product_name = Tran_discount.objects.get(discount_name=key).discount_product_name
                discount_product_discount_category = Tran_discount.objects.get(discount_name=key).discount_product_discount_category
                discount_model = Tran_discount.objects.get(discount_name=key).discount_model
                discount_color = Tran_discount.objects.get(discount_name=key).discount_color
                discount_discount_group = Tran_discount.objects.get(discount_name=key).discount_discount_group
                discount_discount_from = Tran_discount.objects.get(discount_name=key).discount_discount_from
                discount_discount_to = Tran_discount.objects.get(discount_name=key).discount_discount_to
                discount_eff = Tran_discount.objects.get(discount_name=key).discount_eff
                discount_factor = Tran_discount.objects.get(discount_name=key).discount_factor

                row_is_current = Tran_discount.objects.get(discount_name=key).row_is_current
                row_end_date = Tran_discount.objects.get(discount_name=key).row_end_date
                row_change_reason = "normal update"

                dim_discount.update(
                                  discount_customer_id=discount_customer_id
                                , discount_customer_name=discount_customer_name
                                , discount_account_type= discount_account_type
                                , discount_product_id = discount_product_id
                                , discount_product_name = discount_product_name
                                , discount_product_discount_category = discount_product_discount_category
                                , discount_model = discount_model
                                , discount_color = discount_color
                                , discount_discount_group = discount_discount_group
                                , discount_discount_from = discount_discount_from
                                , discount_discount_to = discount_discount_to
                                , discount_eff = discount_eff
                                , discount_factor = discount_factor
                                
                                , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason
                                , import_version = 'v 1.0', import_batch = 0, import_user = 'admin')

                #messages.success(request, 'Form successfully submitted') # Any message you wish
            
            else:
                discount_name = tran_discounts[i].discount_name
                discount_customer_id = tran_discounts[i].discount_customer_id
                discount_customer_name = tran_discounts[i].discount_customer_name
                discount_account_type = tran_discounts[i].discount_account_type
                discount_product_id = tran_discounts[i].discount_product_id
                discount_product_name = tran_discounts[i].discount_product_name
                discount_product_discount_category = tran_discounts[i].discount_product_discount_category
                discount_model = tran_discounts[i].discount_model
                discount_color = tran_discounts[i].discount_color
                discount_discount_group = tran_discounts[i].discount_discount_group
                discount_discount_from = tran_discounts[i].discount_discount_from
                discount_discount_to = tran_discounts[i].discount_discount_to
                discount_eff = tran_discounts[i].discount_eff
                discount_factor = tran_discounts[i].discount_factor

                row_is_current = tran_discounts[i].row_is_current
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                dim_discount = Dim_discount(
                                          discount_name=discount_name
                                        , discount_customer_id=discount_customer_id
                                        , discount_customer_name= discount_customer_name
                                        , discount_account_type = discount_account_type
                                        , discount_product_id = discount_product_id
                                        , discount_product_name = discount_product_name
                                        , discount_product_discount_category = discount_product_discount_category
                                        , discount_model = discount_model
                                        , discount_color = discount_color
                                        , discount_discount_group = discount_discount_group
                                        , discount_discount_from = discount_discount_from
                                        , discount_discount_to = discount_discount_to
                                        , discount_eff = discount_eff
                                        , discount_factor = discount_factor

                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason, import_version = 'v 1.0'
                                        , import_batch = 0
                                        , import_user = 'admin'
                                        )
                dim_discount.save() 
                #messages.success(request, 'Form successfully submitted') # Any message you wish
                #print(str(len(dim_discounts))+' dim_discount update successful')
            from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product_group") 

    number_of_records_imported = Dim_discount.objects.count()
    
    last_import_time = Dim_discount.objects.extra(order_by = ['row_end_date'])

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
    #dim_discount_df = pd.DataFrame(list(Dim_product.objects.all().values()))
    dim_discounts_df = Dim_discount.objects.all()
    dim_discounts_df = read_frame(dim_discounts_df)
    discount_names = dim_discounts_df['discount_name'].values.tolist()
    discount_ids = dim_discounts_df['discount_name'].values.tolist()
    
    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'discount_names':discount_names, 'discount_ids':discount_ids}
             
    
    #print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_discount")
    return render(request, 'dim_discount_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

