from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_sales_order_item, Tran_sales_order_item, Fact_sales_order_item
from dim_color.models import Dim_color
from dim_customer.models import Dim_customer
from dim_product.models import Dim_product
from dim_table.models import Dim_table
from .resources import Stage_sales_order_item_resource, Tran_sales_order_item_resource, Fact_sales_order_item_resource

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
        stage_sales_order_item_resource = Stage_sales_order_item_resource()
        dataset = Dataset()
        new_stage_sales_order_items = request.FILES['myfile']
        stage_sales_order_items = Stage_sales_order_item.objects.all()
        stage_sales_order_items.delete()
        imported_data = dataset.load(new_stage_sales_order_items.read(),format='xlsx') # xlsx

    #     #print(imported_data) 
    #     for data in imported_data:
    #     	print(data[1])
    #     	value = Stage_sales_order_item(
    #      		data[0]               
    #     	,	data[1]
    #     	,	data[2]
    #         ,	data[3]
    #         ,	data[4]
    #         ,	data[5]
    #         ,	data[6]
    #         ,	data[7]
    #         ,	data[8]
    #         ,	data[9]
    #         ,	data[10]             
    #     	,	data[11]
    #     	,	data[12]
    #         ,	data[13]
    #         ,	data[14]
    #         ,	data[15]
    #         ,	data[16]
    #         ,	data[17]
    #         ,	data[18]
    #         ,	data[19]
    #         ,	data[20]             
    #     	,	data[21]
    #     	,	data[22]
    #         ,	data[23]
    #     	)
    #     	value.save()       

    #     #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

    #     #if not result.has_errors():
    #     #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
    #     # updating transform table

    #     # clearing transform table for new data
    #     tran_sales_order_items = Tran_sales_order_item.objects.all()
    #     tran_sales_order_items.delete()
        
    #     # if Stage_sales_order_item.objects.filter(color_temp_key=''): 

    #     #         stage_sales_order_item = Stage_sales_order_item.objects.filter(color_temp_key='')
    #     #         stage_sales_order_item.delete()


    #     stage_sales_order_items = Stage_sales_order_item.objects.all()
    #     length = Stage_sales_order_item.objects.count()
    #     print(str(len(stage_sales_order_items))+' length of stage sales_order_item')

    #     # for i in range(0,len(stage_sales_order_items)-1):
    #     #     day = stage_sales_order_items[i].sales_order_item_order_item  
    #     #     if day == "0000-00-00":
    #     #         day = "2000-01-01"

    #     for i in range(0,len(stage_sales_order_items)):
  
    #         key = stage_sales_order_items[i].sales_order_item_order_item  
    #         if Tran_sales_order_item.objects.filter(sales_order_item_order_item=key).exists(): 

    #             tran_sales_order_item = Tran_sales_order_item.objects.filter(sales_order_item_order_item=key)

    #             sales_order_item_product_category = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_product_category
    #             color_grsales_order_item_warehouseoup = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).color_grsales_order_item_warehouseoup
    #             sales_order_item_site = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_site
    #             sales_order_item_status = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_status
    #             sales_order_item_product = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_product
    #             sales_order_item_product_foreign_key = Dim_product.objects.get(product_id=sales_order_item_product).product_key
    #             sales_order_item_terms = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_terms
    #             sales_order_item_order_item = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_order_item
    #             sales_order_item_po = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_po
    #             sales_order_item_customer_id = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_id
    #             sales_order_item_customer_id_foreign_key = Dim_customer.objects.get(customer_account=sales_order_item_customer_id).customer_key
    #             sales_order_item_customer_name = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_name
    #             sales_order_item_sidemark = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_sidemark
    #             sales_order_item_entered = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_entered
    #             sales_order_item_credit_ok = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_credit_ok
    #             sales_order_item_printed = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_printed
    #             sales_order_item_labels = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_labels
    #             sales_order_item_packed = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_packed
    #             sales_order_item_shipped_date = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_shipped_date
    #             sales_order_item_required = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_required
    #             sales_order_item_canceled = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_canceled
    #             sales_order_item_model = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_model
    #             sales_order_item_color_style = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_color_style
    #             sales_order_item_color_foreign_key = Dim_color.objects.get(color_name=sales_order_item_color_style).color_key
    #             sales_order_item_width = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_width
    #             sales_order_item_height = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_height
    #             sales_order_item_ordered = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_ordered
    #             sales_order_item_shipped_quantity = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_shipped_quantity
    #             sales_order_item_net_sale = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_net_sale
    #             sales_order_item_cost_of_good_sold = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_cost_of_good_sold


    #             row_is_current = "Y"
    #             row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             row_change_reason = "normal update"

    #             tran_sales_order_item.update(color_table=color_table,
    #                                color_group=color_group
    #                              , color_name= color_name
    #                              , color_description = color_description
    #                              , color_bo_date = color_bo_date
    #                              , color_disc_group = color_disc_group
    #                              , color_formula_group = color_formula_group
    #                              , color_begin_date = color_begin_date
    #                              , color_discontinued_date = color_discontinued_date
    #                              , color_inactive_date = color_inactive_date
    #                              , color_constants = color_constants

    #                              , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

    #         else:
    #             color_temp_key = stage_sales_order_items[i].color_temp_key
    #             color_table = stage_sales_order_items[i].color_table
    #             color_group = stage_sales_order_items[i].color_group
    #             color_name = stage_sales_order_items[i].color_name
    #             color_description = stage_sales_order_items[i].color_description
    #             color_bo_date = stage_sales_order_items[i].color_bo_date
    #             color_disc_group = stage_sales_order_items[i].color_disc_group
    #             color_formula_group = stage_sales_order_items[i].color_formula_group
    #             color_begin_date = stage_sales_order_items[i].color_begin_date
    #             color_discontinued_date = stage_sales_order_items[i].color_discontinued_date
    #             color_inactive_date = stage_sales_order_items[i].color_inactive_date
    #             color_constants = stage_sales_order_items[i].color_constants

    #             row_is_current = "Y"
    #             row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             row_change_reason = "original state"

    #             tran_sales_order_item = Tran_sales_order_item(
    #                                           color_temp_key=color_temp_key
    #                                         , color_table=color_table
    #                                         , color_group= color_group
    #                                         , color_name = color_name
    #                                         , color_description = color_description
    #                                         , color_bo_date = color_bo_date
    #                                         , color_disc_group = color_disc_group
    #                                         , color_formula_group = color_formula_group
    #                                         , color_begin_date = color_begin_date
    #                                         , color_discontinued_date = color_discontinued_date
    #                                         , color_inactive_date = color_inactive_date
    #                                         , color_constants = color_constants

    #                                         , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
    #                                         , row_change_reason = row_change_reason
    #                                     )
    #             tran_sales_order_item.save()

    #     print(str(len(stage_sales_order_items))+' tran_sales_order_item update successful')
    #     # loading to datawarehouse tabel
    #     tran_sales_order_items = Tran_sales_order_item.objects.all()
    #     length = Tran_sales_order_item.objects.count()
    #     print(str(len(tran_sales_order_items)) + " sales_order_items in transform table")
    #     for i in range(0,len(tran_sales_order_items)):
            
    #         key = tran_sales_order_items[i].sales_order_item_temp_key  
    #         if Fact_sales_order_item.objects.filter(color_unique_key=key).exists(): 

    #             fact_sales_order_item = Fact_sales_order_item.objects.filter(color_unique_key=key)

    #             color_unique_key = Tran_sales_order_item.objects.get(color_unique_key=key).color_temp_key
    #             color_table = Tran_sales_order_item.objects.get(color_unique_key=key).color_table
    #             color_group = Tran_sales_order_item.objects.get(color_unique_key=key).color_group
    #             color_name = Tran_sales_order_item.objects.get(color_unique_key=key).color_name
    #             color_description = Tran_sales_order_item.objects.get(color_unique_key=key).color_description
    #             color_bo_date = Tran_sales_order_item.objects.get(color_unique_key=key).color_bo_date
    #             color_disc_group = Tran_sales_order_item.objects.get(color_unique_key=key).color_disc_group
    #             color_formula_group = Tran_sales_order_item.objects.get(color_unique_key=key).color_formula_group
    #             color_begin_date = Tran_sales_order_item.objects.get(color_unique_key=key).color_begin_date
    #             color_discontinued_date = Tran_sales_order_item.objects.get(color_unique_key=key).color_discontinued_date
    #             color_inactive_date = Tran_sales_order_item.objects.get(color_unique_key=key).color_inactive_date
    #             color_constants = Tran_sales_order_item.objects.get(color_unique_key=key).color_constants
                
    #             row_is_current = Tran_sales_order_item.objects.get(color_unique_key=key).row_is_current
    #             row_end_date = Tran_sales_order_item.objects.get(color_unique_key=key).row_end_date
    #             row_change_reason = "normal update"

    #             dim_color.update(
    #                               color_unique_key=color_unique_key
    #                             , color_table=color_table
    #                             , color_group= color_group
    #                             , color_name = color_name
    #                             , color_description = color_description
    #                             , color_bo_date = color_bo_date
    #                             , color_disc_group = color_disc_group
    #                             , color_formula_group = color_formula_group
    #                             , color_begin_date = color_begin_date
    #                             , color_discontinued_date = color_discontinued_date
    #                             , color_inactive_date = color_inactive_date
    #                             , color_constants = color_constants
                                
                            
    #                             , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason
    #                             , import_version = 'v 1.0', import_batch = 0, import_user = 'admin')

    #             #messages.success(request, 'Form successfully submitted') # Any message you wish
            
    #         else:
    #             color_unique_key = tran_sales_order_items[i].color_temp_key
    #             color_table = tran_sales_order_items[i].color_table
    #             color_group = tran_sales_order_items[i].color_group
    #             color_name = tran_sales_order_items[i].color_name
    #             color_description = tran_sales_order_items[i].color_description
    #             color_bo_date = tran_sales_order_items[i].color_bo_date
    #             color_disc_group = tran_sales_order_items[i].color_disc_group
    #             color_formula_group = tran_sales_order_items[i].color_formula_group
    #             color_begin_date = tran_sales_order_items[i].color_begin_date
    #             color_discontinued_date = tran_sales_order_items[i].color_discontinued_date
    #             color_inactive_date = tran_sales_order_items[i].color_inactive_date
    #             color_constants = tran_sales_order_items[i].color_constants
                
    #             row_is_current = tran_sales_order_items[i].row_is_current
    #             row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #             row_change_reason = "original state"

    #             fact_sales_order_item = Fact_sales_order_item(
    #                                       color_unique_key=color_unique_key
    #                                     , color_table=color_table
    #                                     , color_group= color_group
    #                                     , color_name = color_name
    #                                     , color_description = color_description
    #                                     , color_bo_date = color_bo_date
    #                                     , color_disc_group = color_disc_group
    #                                     , color_formula_group = color_formula_group
    #                                     , color_begin_date = color_begin_date
    #                                     , color_discontinued_date = color_discontinued_date
    #                                     , color_inactive_date = color_inactive_date
    #                                     , color_constants = color_constants
                                                                    
    #                                     , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
    #                                     , row_change_reason = row_change_reason, import_version = 'v 1.0'
    #                                     , import_batch = 0
    #                                     , import_user = 'admin'
    #                                     )
    #             fact_sales_order_item.save() 
    #             #messages.success(request, 'Form successfully submitted') # Any message you wish
    #             #print(str(len(dim_sales_order_items))+' fact_sales_order_item update successful')
    #         from django.http import HttpResponseRedirect
    #         #return HttpResponseRedirect("/dim_product_group") 

    # number_of_records_imported = Fact_sales_order_item.objects.count()
    
    # last_import_time = Fact_sales_order_item.objects.extra(order_by = ['row_end_date'])

    # # ---------------------------------------------------------------------------------------------------------------------------------------------
    # # Use this block after table is added to dim_table

    # # last_import_time = last_import_time[number_of_records_imported-1].row_end_date
    # # table = Dim_table.objects.filter(table_name='jcwf_dim_product_group')
    # # tablename = Dim_table.objects.get(table_name='jcwf_dim_product_group').table_name
    # # table.update(number_of_records_imported=number_of_records_imported, row_end_date=last_import_time
    # #            , row_change_reason = 'normal update')

    # # last_import_time = Dim_table.objects.get(table_name='jcwf_dim_product_group').row_end_date 
    # # total_records = Dim_table.objects.get(table_name='jcwf_dim_product_group').number_of_records_imported 

    # # ---------------------------------------------------------------------------------------------------------------------------------------------
    # # Use this block before table is added to dim_table

    # tablename = 'test'
    # last_import_time = '8/3/2021'
    # total_records = 'test'

    # # ---------------------------------------------------------------------------------------------------------------------------------------------
    # #dim_sales_order_items_df = pd.DataFrame(list(Dim_product.objects.all().values()))
    # fact_sales_order_items_df = Fact_sales_order_item.objects.all()
    # fact_sales_order_items_df = read_frame(fact_sales_order_items_df)
    # sales_order_items_names = fact_sales_order_items_df['sales_order_items_name'].values.tolist()
    # sales_order_items_ids = fact_sales_order_items_df['color_unique_key'].values.tolist()
    
    # context = {'tablename':tablename, 'last_import_time':last_import_time
    #          , 'total_records':total_records, 'color_names':color_names, 'color_ids':color_ids}
             
    
    # #print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_color")
    return render(request, 'dim_color_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

