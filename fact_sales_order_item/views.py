from django.shortcuts import render, redirect
from .models import Stage_sales_order_item, Tran_sales_order_item, Fact_sales_order_item
from dim_table.models import Dim_table
from .resources import Stage_sales_order_item_resource, Tran_sales_order_item_resource, Fact_sales_order_item_resource
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
import pandas as pd
from fact_sales_order_item.query_function import etl_query
from datetime import datetime
import time

# app_start_time = datetime.now()

@login_required(login_url="/accounts/login/")
def simple_upload(request): 
    # app_start_time = datetime.now()
    if request.method == 'POST':

        app_start_time = datetime.now()
        stage_sales_order_item_resource = Stage_sales_order_item_resource()
        stage_sales_order_items = Stage_sales_order_item.objects.all()
        stage_sales_order_items.delete()

        map_row = ['sales_order_item_product_category'
                 , 'sales_order_item_warehouse'
                 , 'sales_order_item_site'
                 , 'sales_order_item_status'
                 , 'sales_order_item_product'
                 , 'sales_order_item_terms' 
                 , 'sales_order_item_order_item'  
                 , 'sales_order_item_po'  
                 , 'sales_order_item_customer_id' 
                 , 'sales_order_item_customer_name' 
                 , 'sales_order_item_sidemark' 
                 , 'sales_order_item_entered' 
                 , 'sales_order_item_credit_ok'  
                 , 'sales_order_item_printed' 
                 , 'sales_order_item_labels' 
                 , 'sales_order_item_packed' 
                 , 'sales_order_item_shipped_date' 
                 , 'sales_order_item_required' 
                 , 'sales_order_item_canceled' 
                 , 'sales_order_item_model' 
                 , 'sales_order_item_color_style' 
                 , 'sales_order_item_width' 
                 , 'sales_order_item_height'
                 , 'sales_order_item_ordered' 
                 , 'sales_order_item_shipped_quantity' 
                 , 'sales_order_item_net_sale'
                 , 'sales_order_item_cost_of_good_sold'
                 ]

        request.FILES["myfile"].save_to_database(   
            model=Stage_sales_order_item,
            mapdict=map_row
        )
        etl_query()

    # post import ----------------------------------------------------------------------------------------------------------------------------------
    number_of_records_imported = Fact_sales_order_item.objects.count()
    last_import_time = Fact_sales_order_item.objects.extra(order_by = ['row_end_date'])

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block after table is added to dim_table

    # last_import_time = last_import_time[number_of_records_imported-1].row_end_date
    # table = Dim_table.objects.filter(table_name='jcwf_dim_product_group')
    # tablename = Dim_table.objects.get(table_name='jcwf_dim_product_group').table_name
    # table.update(number_of_records_imported=number_of_records_imported
    #            , row_end_date=last_import_time
    #            , row_change_reason = 'normal update')
    # last_import_time = Dim_table.objects.get(table_name='jcwf_dim_product_group').row_end_date 
    # total_records = Dim_table.objects.get(table_name='jcwf_dim_product_group').number_of_records_imported 

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block before table is added to dim_table
    tablename = 'test'
    last_import_time = '8/3/2021'
    total_records = 'test'

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    #dim_sales_order_items_df = pd.DataFrame(list(Dim_product.objects.all().values()))

    # fact_sales_order_items_df = Fact_sales_order_item.objects.all()
    # fact_sales_order_items_df = read_frame(fact_sales_order_items_df)
    # sales_order_items_names = fact_sales_order_items_df['sales_order_items_name'].values.tolist()
    # sales_order_items_ids = fact_sales_order_items_df['sales_order_item_order_item'].values.tolist()
    sales_order_items_names = 'test'
    sales_order_items_ids = 'test'

    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'sales_order_items_names':sales_order_items_names
             , 'sales_order_items_ids':sales_order_items_ids}
    print("duration \n")
    print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    return render(request, 'fact_sales_order_item_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')
