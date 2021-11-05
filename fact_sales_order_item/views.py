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

import psycopg2
import pandas as pd
from pandas import DataFrame
import time

from fact_sales_order_item.test_function import do_something

# Create your views here.
app_start_time = datetime.now()



@login_required(login_url="/accounts/login/")
def simple_upload(request):

    if request.method == 'POST':

        app_start_time = datetime.now()

        # stage table --------------------------------------------------------------------------------------------------------------------------
        # updating stage table
        stage_sales_order_item_resource = Stage_sales_order_item_resource()
        dataset = Dataset()
        new_stage_sales_order_items = request.FILES['myfile']
        # stage_sales_order_items = Stage_sales_order_item.objects.all()
        # stage_sales_order_items.delete()
        imported_data = dataset.load(new_stage_sales_order_items.read(),format='xlsx') # xlsx
        # print(imported_data) 
        
        datass = pd.DataFrame(columns=[
              'sales_order_item_product_category'  
            , 'sales_order_item_warehouse'  
            , 'sales_order_item_site' 
            , 'sales_order_item_status' 
            , 'sales_order_item_product' 
            , 'sales_order_item_product_foreign_key'
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
            ])

        # x_record = pd.Series(['hi','today'])

        for data in imported_data:
            datass = datass.append({
                'sales_order_item_product_category': data[0] 
                , 'sales_order_item_warehouse': data[1] 
                , 'sales_order_item_site': data[2]  
                , 'sales_order_item_status': data[3]  
                , 'sales_order_item_product': data[4]  
                , 'sales_order_item_terms': data[5] 
                , 'sales_order_item_order_item': data[6]  
                , 'sales_order_item_po': data[7]   
                , 'sales_order_item_customer_id': data[8]   
                , 'sales_order_item_customer_name': data[9]  
                , 'sales_order_item_sidemark': data[10]  
                , 'sales_order_item_entered': data[11]  
                , 'sales_order_item_credit_ok': data[12]  
                , 'sales_order_item_printed': data[13]   
                , 'sales_order_item_labels': data[14]  
                , 'sales_order_item_packed': data[15]  
                , 'sales_order_item_shipped_date': data[16]  
                , 'sales_order_item_required': data[17]  
                , 'sales_order_item_canceled': data[18]  
                , 'sales_order_item_model': data[19]  
                , 'sales_order_item_color_style': data[20]  
                , 'sales_order_item_width': data[21]  
                , 'sales_order_item_height': data[22]  
                , 'sales_order_item_ordered': data[23] 
                , 'sales_order_item_shipped_quantity': data[24] 
                , 'sales_order_item_net_sale': data[25]  
                , 'sales_order_item_cost_of_good_sold': data[26] 
                                    }, ignore_index=True)
        # print(datass)


        import psycopg2


        df = datass
        conn = psycopg2.connect("host='econometricdatasolutionsdb.postgres.database.azure.com' dbname=postgres user='Christopher@econometricdatasolutionsdb' password='Darkknight17!'")
        cur = conn.cursor()
        cur.execute("""   
        /* Updating transformation table */
        TRUNCATE jcwf_stage_sales_order_item;
        """
        )
        conn.commit()
        conn.close()
        
        conn = psycopg2.connect("host='econometricdatasolutionsdb.postgres.database.azure.com' dbname=postgres user='Christopher@econometricdatasolutionsdb' password='Darkknight17!'")
        cur = conn.cursor()
        for index, row in df.iterrows():

            insertdata =  "('"+str(row[0]).replace("\'", "")+"','"+str(row[1]).replace("\'", "")+"','"+str(row[2]).replace("\'", "")+"','"+str(row[3]).replace("\'", "")+"','"+str(row[4]).replace("\'", "")+"','"+str(row[5]).replace("\'", "")+"','"+str(row[6]).replace("\'", "")+"','"+str(row[7]).replace("\'", "")+"','"+str(row[8]).replace("\'", "")+"','"+str(row[9]).replace("\'", "")+"','"+str(row[10]).replace("\'", "")+"','"+str(row[11]).replace("\'", "")+"','"+str(row[12]).replace("\'", "")+"','"+str(row[13]).replace("\'", "")+"','"+str(row[14]).replace("\'", "")+"','"+str(row[15]).replace("\'", "")+"','"+str(row[16]).replace("\'", "")+"','"+str(row[17]).replace("\'", "")+"','"+str(row[18]).replace("\'", "")+"','"+str(row[19]).replace("\'", "")+"','"+str(row[20]).replace("\'", "")+"','"+str(row[21]).replace("\'", "")+"','"+str(row[22]).replace("\'", "")+"','"+str(row[23]).replace("\'", "")+"','"+str(row[24]).replace("\'", "")+"','"+str(row[25]).replace("\'", "")+"','"+str(row[26]).replace("\'", "")+"');"
            print("insertdata :",insertdata)
            try:
                cur.execute(
                    """ INSERT INTO jcwf_stage_sales_order_item values """ +insertdata)

                print( "row inserted:", insertdata)
            except psycopg2.IntegrityError:


                print( "Row already exist ")
                pass 
            except Exception as e:

                print("some insert error:", e, "ins: ", insertdata)
        conn.commit()   
        conn.close()















        '''

        #print(imported_data) 
        print(type(imported_data))
        for data in imported_data:
        	print(data[1])
        	value = Stage_sales_order_item(  
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
            ,	data[14]
            ,	data[15]
            ,	data[16]
            ,	data[17]
            ,	data[18]
            ,	data[19]
            ,	data[20]             
        	,	data[21]
        	,	data[22]
            ,	data[23]
            ,	data[24]
            ,	data[25]
            ,	data[26]
        	)
        	# value.save()       
            
        do_something()
        '''

        # time.sleep(60)
    # importing data from the data warehouse using psycopg2
    # import psycopg2
    # import pandas as pd
    # from pandas import DataFrame
    # import time
    # conn = psycopg2.connect() #"host='econometricdatasolutionsdb.postgres.database.azure.com' dbname=postgres user='Christopher@econometricdatasolutionsdb' password='Darkknight17!'"
    # cur = conn.cursor()
    # cur.execute("""
    
    # /* Updating transformation table */
    # insert INTO jcwf_tran_sales_order_item (

    # sales_order_item_product_category  
    # , sales_order_item_warehouse  
    # , sales_order_item_site 
    # , sales_order_item_status 
    # , sales_order_item_product 
    # , sales_order_item_product_foreign_key
    # , sales_order_item_terms 
    # , sales_order_item_order_item  
    # , sales_order_item_po  
    # , sales_order_item_customer_id 
    # , sales_order_item_customer_name 
    # , sales_order_item_sidemark 
    # , sales_order_item_entered 
    # , sales_order_item_credit_ok  
    # , sales_order_item_printed 
    # , sales_order_item_labels 
    # , sales_order_item_packed 
    # , sales_order_item_shipped_date 
    # , sales_order_item_required 
    # , sales_order_item_canceled 
    # , sales_order_item_model 
    # , sales_order_item_color_style 
    # , sales_order_item_width 
    # , sales_order_item_height
    # , sales_order_item_ordered 
    # , sales_order_item_shipped_quantity 
    # , sales_order_item_net_sale
    # , sales_order_item_cost_of_good_sold


    # )

    # SELECT 

    # sales_order_item_product_category  
    # , sales_order_item_warehouse  
    # , sales_order_item_site 
    # , sales_order_item_status 
    # , sales_order_item_product 
    # , (SELECT product_key FROM jcwf_dim_product WHERE jcwf_dim_product.product_id = jcwf_stage_sales_order_item.sales_order_item_product) AS sales_order_item_product_foreign_key
    # , sales_order_item_terms 
    # , sales_order_item_order_item  
    # , sales_order_item_po  
    # , sales_order_item_customer_id 
    # , sales_order_item_customer_name 
    # , sales_order_item_sidemark 
    # , sales_order_item_entered 
    # , sales_order_item_credit_ok  
    # , sales_order_item_printed 
    # , sales_order_item_labels 
    # , sales_order_item_packed 
    # , sales_order_item_shipped_date 
    # , sales_order_item_required 
    # , sales_order_item_canceled 
    # , sales_order_item_model 
    # , sales_order_item_color_style 
    # , sales_order_item_width 
    # , sales_order_item_height
    # , sales_order_item_ordered 
    # , sales_order_item_shipped_quantity 
    # , sales_order_item_net_sale
    # , sales_order_item_cost_of_good_sold

    # from jcwf_stage_sales_order_item

    # ON CONFLICT ON CONSTRAINT Unique_jcwf_tran_sales_order_item_id DO UPDATE set 

    # sales_order_item_product_category = excluded.sales_order_item_product_category
    # , sales_order_item_warehouse = excluded.sales_order_item_warehouse
    # , sales_order_item_site = excluded.sales_order_item_site
    # , sales_order_item_status = excluded.sales_order_item_status
    # , sales_order_item_product = excluded.sales_order_item_product
    # , sales_order_item_product_foreign_key = excluded.sales_order_item_product_foreign_key
    # , sales_order_item_terms = excluded.sales_order_item_terms
    # , sales_order_item_order_item = excluded.sales_order_item_order_item
    # , sales_order_item_po = excluded.sales_order_item_po
    # , sales_order_item_customer_id = excluded.sales_order_item_customer_id
    # , sales_order_item_customer_name = excluded.sales_order_item_customer_name
    # , sales_order_item_sidemark = excluded.sales_order_item_sidemark
    # , sales_order_item_entered = excluded.sales_order_item_entered
    # , sales_order_item_credit_ok = excluded.sales_order_item_credit_ok
    # , sales_order_item_printed = excluded.sales_order_item_printed
    # , sales_order_item_labels = excluded.sales_order_item_labels
    # , sales_order_item_packed = excluded.sales_order_item_packed
    # , sales_order_item_shipped_date = excluded.sales_order_item_shipped_date
    # , sales_order_item_required = excluded.sales_order_item_required
    # , sales_order_item_canceled = excluded.sales_order_item_canceled
    # , sales_order_item_model = excluded.sales_order_item_model
    # , sales_order_item_color_style = excluded.sales_order_item_color_style
    # , sales_order_item_width = excluded.sales_order_item_width
    # , sales_order_item_height = excluded.sales_order_item_height
    # , sales_order_item_ordered = excluded.sales_order_item_ordered
    # , sales_order_item_shipped_quantity = excluded.sales_order_item_shipped_quantity
    # , sales_order_item_net_sale = excluded.sales_order_item_net_sale
    # , sales_order_item_cost_of_good_sold = excluded.sales_order_item_cost_of_good_sold;

    # -------------------------------------------------------------------------------------------------------
    # /* Updating fact table */
    # insert INTO jcwf_fact_sales_order_item (

    # sales_order_item_product_category  
    # , sales_order_item_warehouse  
    # , sales_order_item_site 
    # , sales_order_item_status 
    # , sales_order_item_product_foreign_key
    # , sales_order_item_terms 
    # , sales_order_item_order_item  
    # , sales_order_item_po  
    # , sales_order_item_customer_id_foreign_key 
    # , sales_order_item_sidemark 
    # , sales_order_item_entered 
    # , sales_order_item_credit_ok  
    # , sales_order_item_printed 
    # , sales_order_item_labels 
    # , sales_order_item_packed 
    # , sales_order_item_shipped_date 
    # , sales_order_item_required 
    # , sales_order_item_canceled 
    # , sales_order_item_model 
    # , sales_order_item_color_foreign_key 
    # , sales_order_item_width 
    # , sales_order_item_height
    # , sales_order_item_ordered 
    # , sales_order_item_shipped_quantity 
    # , sales_order_item_net_sale
    # , sales_order_item_cost_of_good_sold


    # )

    # SELECT 

    # sales_order_item_product_category  
    # , sales_order_item_warehouse  
    # , sales_order_item_site 
    # , sales_order_item_status 
    # , sales_order_item_product_foreign_key
    # , sales_order_item_terms 
    # , sales_order_item_order_item  
    # , sales_order_item_po  
    # , sales_order_item_customer_id_foreign_key 
    # , sales_order_item_sidemark 
    # , sales_order_item_entered 
    # , sales_order_item_credit_ok  
    # , sales_order_item_printed 
    # , sales_order_item_labels 
    # , sales_order_item_packed 
    # , sales_order_item_shipped_date 
    # , sales_order_item_required 
    # , sales_order_item_canceled 
    # , sales_order_item_model 
    # , sales_order_item_color_foreign_key 
    # , sales_order_item_width 
    # , sales_order_item_height
    # , sales_order_item_ordered 
    # , sales_order_item_shipped_quantity 
    # , sales_order_item_net_sale
    # , sales_order_item_cost_of_good_sold

    # from jcwf_tran_sales_order_item

    # ON CONFLICT ON CONSTRAINT Unique_fact_sales_order_item DO UPDATE set 

    # sales_order_item_product_category = excluded.sales_order_item_product_category
    # , sales_order_item_warehouse = excluded.sales_order_item_warehouse
    # , sales_order_item_site = excluded.sales_order_item_site
    # , sales_order_item_status = excluded.sales_order_item_status
    # , sales_order_item_product_foreign_key = excluded.sales_order_item_product_foreign_key
    # , sales_order_item_terms = excluded.sales_order_item_terms
    # , sales_order_item_order_item = excluded.sales_order_item_order_item
    # , sales_order_item_po = excluded.sales_order_item_po
    # , sales_order_item_customer_id_foreign_key = excluded.sales_order_item_customer_id_foreign_key
    # , sales_order_item_sidemark = excluded.sales_order_item_sidemark
    # , sales_order_item_entered = excluded.sales_order_item_entered
    # , sales_order_item_credit_ok = excluded.sales_order_item_credit_ok
    # , sales_order_item_printed = excluded.sales_order_item_printed
    # , sales_order_item_labels = excluded.sales_order_item_labels
    # , sales_order_item_packed = excluded.sales_order_item_packed
    # , sales_order_item_shipped_date = excluded.sales_order_item_shipped_date
    # , sales_order_item_required = excluded.sales_order_item_required
    # , sales_order_item_canceled = excluded.sales_order_item_canceled
    # , sales_order_item_model = excluded.sales_order_item_model
    # , sales_order_item_color_foreign_key = excluded.sales_order_item_color_foreign_key
    # , sales_order_item_width = excluded.sales_order_item_width
    # , sales_order_item_height = excluded.sales_order_item_height
    # , sales_order_item_ordered = excluded.sales_order_item_ordered
    # , sales_order_item_shipped_quantity = excluded.sales_order_item_shipped_quantity
    # , sales_order_item_net_sale = excluded.sales_order_item_net_sale
    # , sales_order_item_cost_of_good_sold = excluded.sales_order_item_cost_of_good_sold;

    # SELECT * FROM jcwf_fact_sales_order_item;

    # """
    # )
    
    # print('testing out psycopg2 speed')











#------------------------------------------------------------------------------------------------------
        # #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        # #if not result.has_errors():
        # #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        # # updating transform table

        # # clearing transform table for new data
        # tran_sales_order_items = Tran_sales_order_item.objects.all()
        # tran_sales_order_items.delete()
        
        # # if Stage_sales_order_item.objects.filter(color_temp_key=''): 

        # #         stage_sales_order_item = Stage_sales_order_item.objects.filter(color_temp_key='')
        # #         stage_sales_order_item.delete()


        # stage_sales_order_items = Stage_sales_order_item.objects.all()
        # length = Stage_sales_order_item.objects.count()
        # print(str(len(stage_sales_order_items))+' length of stage sales_order_item')

        # # for i in range(0,len(stage_sales_order_items)-1):
        # #     day = stage_sales_order_items[i].sales_order_item_order_item  
        # #     if day == "0000-00-00":
        # #         day = "2000-01-01"

        # # Transformation table --------------------------------------------------------------------------------------------------------------------------
        # for i in range(0,len(stage_sales_order_items)):
  
        #     key = stage_sales_order_items[i].sales_order_item_order_item  
        #     if Tran_sales_order_item.objects.filter(sales_order_item_order_item=key).exists(): 

        #         tran_sales_order_item = Tran_sales_order_item.objects.filter(sales_order_item_order_item=key)

        #         sales_order_item_product_category = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_product_category
        #         sales_order_item_warehouse = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_warehouse
        #         sales_order_item_site = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_site
        #         sales_order_item_status = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_status
        #         sales_order_item_product = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_product
        #         sales_order_item_product_foreign_key = 'test' #Dim_product.objects.get(product_id=sales_order_item_product).product_key
        #         sales_order_item_terms = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_terms
        #         sales_order_item_order_item = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_order_item
        #         sales_order_item_po = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_po
        #         sales_order_item_customer_id = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_id
        #         sales_order_item_customer_id_foreign_key = 'test' #Dim_customer.objects.get(customer_account=sales_order_item_customer_id).customer_key
        #         sales_order_item_customer_name = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_name
        #         sales_order_item_sidemark = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_sidemark
        #         sales_order_item_entered = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_entered
        #         sales_order_item_credit_ok = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_credit_ok
        #         sales_order_item_printed = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_printed
        #         sales_order_item_labels = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_labels
        #         sales_order_item_packed = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_packed
        #         sales_order_item_shipped_date = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_shipped_date
        #         sales_order_item_required = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_required
        #         sales_order_item_canceled = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_canceled
        #         sales_order_item_model = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_model
        #         sales_order_item_color_style = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_color_style
        #         sales_order_item_color_foreign_key = Dim_color.objects.get(color_name=sales_order_item_color_style).color_key
        #         sales_order_item_width = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_width
        #         sales_order_item_height = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_height
        #         sales_order_item_ordered = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_ordered
        #         sales_order_item_shipped_quantity = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_shipped_quantity
        #         sales_order_item_net_sale = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_net_sale
        #         sales_order_item_cost_of_good_sold = Stage_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_cost_of_good_sold


        #         row_is_current = "Y"
        #         row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #         row_change_reason = "normal update"

        #         tran_sales_order_item.update(sales_order_item_product_category=sales_order_item_product_category
        #                          , sales_order_item_warehouse=sales_order_item_warehouse
        #                          , sales_order_item_site= sales_order_item_site
        #                          , sales_order_item_status = sales_order_item_status
        #                          , sales_order_item_product = sales_order_item_product
        #                          , sales_order_item_product_foreign_key = sales_order_item_product_foreign_key
        #                          , sales_order_item_terms = sales_order_item_terms
        #                          , sales_order_item_order_item = sales_order_item_order_item
        #                          , sales_order_item_po = sales_order_item_po
        #                          , sales_order_item_customer_id = sales_order_item_customer_id
        #                          , sales_order_item_customer_id_foreign_key = '1' #sales_order_item_customer_id_foreign_key
        #                          , sales_order_item_customer_name = sales_order_item_customer_name
        #                          , sales_order_item_sidemark = sales_order_item_sidemark
        #                          , sales_order_item_entered = sales_order_item_entered
        #                          , sales_order_item_credit_ok = sales_order_item_credit_ok
        #                          , sales_order_item_printed = sales_order_item_printed
        #                          , sales_order_item_labels = sales_order_item_labels
        #                          , sales_order_item_packed = sales_order_item_packed
        #                          , sales_order_item_shipped_date = sales_order_item_shipped_date
        #                          , sales_order_item_required = sales_order_item_required
        #                          , sales_order_item_canceled = sales_order_item_canceled
        #                          , sales_order_item_model = sales_order_item_model
        #                          , sales_order_item_color_style = sales_order_item_color_style
        #                          , sales_order_item_color_foreign_key = sales_order_item_color_foreign_key
        #                          , sales_order_item_width = sales_order_item_width
        #                          , sales_order_item_height = sales_order_item_height
        #                          , sales_order_item_ordered = sales_order_item_ordered
        #                          , sales_order_item_shipped_quantity = sales_order_item_shipped_quantity
        #                          , sales_order_item_net_sale = sales_order_item_net_sale
        #                          , sales_order_item_cost_of_good_sold = sales_order_item_cost_of_good_sold

        #                          , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

        #     else:
        #         sales_order_item_product_category = stage_sales_order_items[i].sales_order_item_product_category
        #         sales_order_item_warehouse = stage_sales_order_items[i].sales_order_item_warehouse
        #         sales_order_item_site = stage_sales_order_items[i].sales_order_item_site
        #         sales_order_item_status = stage_sales_order_items[i].sales_order_item_status
        #         sales_order_item_product = stage_sales_order_items[i].sales_order_item_product
        #         sales_order_item_product_foreign_key = '1'
        #         sales_order_item_terms = stage_sales_order_items[i].sales_order_item_terms
        #         sales_order_item_order_item = stage_sales_order_items[i].sales_order_item_order_item
        #         sales_order_item_po = stage_sales_order_items[i].sales_order_item_po
        #         sales_order_item_customer_id = stage_sales_order_items[i].sales_order_item_customer_id
        #         sales_order_item_customer_id_foreign_key = '1' #
        #         sales_order_item_customer_name = stage_sales_order_items[i].sales_order_item_customer_name
        #         sales_order_item_sidemark = stage_sales_order_items[i].sales_order_item_sidemark
        #         sales_order_item_entered = stage_sales_order_items[i].sales_order_item_entered
        #         sales_order_item_credit_ok = stage_sales_order_items[i].sales_order_item_credit_ok
        #         sales_order_item_printed = stage_sales_order_items[i].sales_order_item_printed
        #         sales_order_item_labels = stage_sales_order_items[i].sales_order_item_labels
        #         sales_order_item_packed = stage_sales_order_items[i].sales_order_item_packed
        #         sales_order_item_shipped_date = stage_sales_order_items[i].sales_order_item_shipped_date
        #         sales_order_item_required = stage_sales_order_items[i].sales_order_item_required
        #         sales_order_item_canceled = stage_sales_order_items[i].sales_order_item_canceled
        #         sales_order_item_model = stage_sales_order_items[i].sales_order_item_model
        #         sales_order_item_color_style = stage_sales_order_items[i].sales_order_item_color_style
        #         # sales_order_item_color_foreign_key = stage_sales_order_items[i].color_constants
        #         sales_order_item_width = stage_sales_order_items[i].sales_order_item_width
        #         sales_order_item_height = stage_sales_order_items[i].sales_order_item_height
        #         sales_order_item_ordered = stage_sales_order_items[i].sales_order_item_ordered
        #         sales_order_item_shipped_quantity = stage_sales_order_items[i].sales_order_item_shipped_quantity
        #         sales_order_item_net_sale = stage_sales_order_items[i].sales_order_item_net_sale
        #         sales_order_item_cost_of_good_sold = stage_sales_order_items[i].sales_order_item_cost_of_good_sold

        #         row_is_current = "Y"
        #         row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #         row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #         row_change_reason = "original state"

        #         tran_sales_order_item = Tran_sales_order_item(
        #                                       sales_order_item_product_category=sales_order_item_product_category
        #                                     , sales_order_item_warehouse=sales_order_item_warehouse
        #                                     , sales_order_item_site= sales_order_item_site
        #                                     , sales_order_item_status = sales_order_item_status
        #                                     , sales_order_item_product = sales_order_item_product
        #                                     , sales_order_item_product_foreign_key = '1'
        #                                     , sales_order_item_terms = sales_order_item_terms
        #                                     , sales_order_item_order_item = sales_order_item_order_item
        #                                     , sales_order_item_po = sales_order_item_po
        #                                     , sales_order_item_customer_id = sales_order_item_customer_id
        #                                     , sales_order_item_customer_id_foreign_key = '1' #sales_order_item_customer_id_foreign_key
        #                                     , sales_order_item_customer_name = sales_order_item_customer_name
        #                                     , sales_order_item_sidemark = sales_order_item_sidemark
        #                                     , sales_order_item_entered = sales_order_item_entered
        #                                     , sales_order_item_credit_ok = sales_order_item_credit_ok
        #                                     , sales_order_item_printed = sales_order_item_printed
        #                                     , sales_order_item_labels = sales_order_item_labels
        #                                     , sales_order_item_packed = sales_order_item_packed
        #                                     , sales_order_item_shipped_date = sales_order_item_shipped_date
        #                                     , sales_order_item_required = sales_order_item_required
        #                                     , sales_order_item_canceled = sales_order_item_canceled
        #                                     , sales_order_item_model = sales_order_item_model
        #                                     , sales_order_item_color_style = sales_order_item_color_style
        #                                     # , sales_order_item_color_foreign_key = sales_order_item_color_foreign_key
        #                                     , sales_order_item_width = sales_order_item_width
        #                                     , sales_order_item_height = sales_order_item_height
        #                                     , sales_order_item_ordered = sales_order_item_ordered
        #                                     , sales_order_item_shipped_quantity = sales_order_item_shipped_quantity
        #                                     , sales_order_item_net_sale = sales_order_item_net_sale
        #                                     , sales_order_item_cost_of_good_sold = sales_order_item_cost_of_good_sold

        #                                     , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
        #                                     , row_change_reason = row_change_reason
        #                                 )
        #         tran_sales_order_item.save()

        # print(str(len(stage_sales_order_items))+' tran_sales_order_item update successful')
        # # loading to datawarehouse tabel
        # tran_sales_order_items = Tran_sales_order_item.objects.all()
        # length = Tran_sales_order_item.objects.count()
        # print(str(len(tran_sales_order_items)) + " sales_order_items in transform table")

        # # Datawarehouse table --------------------------------------------------------------------------------------------------------------------------
        # for i in range(0,len(tran_sales_order_items)):
            
        #     key = tran_sales_order_items[i].sales_order_item_order_item  
        #     if Fact_sales_order_item.objects.filter(sales_order_item_order_item=key).exists(): 

        #         fact_sales_order_item = Fact_sales_order_item.objects.filter(sales_order_item_order_item=key)

        #         sales_order_item_product_category = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_product_category
        #         sales_order_item_warehouse = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_warehouse
        #         sales_order_item_site = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_site
        #         sales_order_item_status = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_status
        #         sales_order_item_product = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_product
        #         sales_order_item_product_foreign_key = '1'
        #         sales_order_item_terms = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_terms
        #         sales_order_item_order_item = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_order_item
        #         sales_order_item_po = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_po
        #         sales_order_item_customer_id = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_id
        #         sales_order_item_customer_id_foreign_key = '1' #Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_id_foreign_key
        #         sales_order_item_customer_name = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_customer_name
        #         sales_order_item_sidemark = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_sidemark 
        #         sales_order_item_entered = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_entered
        #         sales_order_item_credit_ok = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_credit_ok
        #         sales_order_item_printed = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_printed
        #         sales_order_item_labels = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_labels
        #         sales_order_item_packed = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_packed
        #         sales_order_item_shipped_date = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_shipped_date
        #         sales_order_item_required = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_required
        #         sales_order_item_canceled = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_canceled
        #         sales_order_item_model = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_model
        #         sales_order_item_color_style = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_color_style
        #         sales_order_item_color_foreign_key = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_color_foreign_key
        #         sales_order_item_width = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_width
        #         sales_order_item_height = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_height
        #         sales_order_item_ordered = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_ordered
        #         sales_order_item_shipped_quantity = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_shipped_quantity
        #         sales_order_item_net_sale = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_net_sale
        #         sales_order_item_cost_of_good_sold = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).sales_order_item_cost_of_good_sold





        #         row_is_current = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).row_is_current
        #         row_end_date = Tran_sales_order_item.objects.get(sales_order_item_order_item=key).row_end_date
        #         row_change_reason = "normal update"

        #         fact_sales_order_item.update(
        #                           sales_order_item_product_category=sales_order_item_product_category
        #                         , sales_order_item_warehouse=sales_order_item_warehouse
        #                         , sales_order_item_site= sales_order_item_site
        #                         , sales_order_item_status = sales_order_item_status
        #                         # , sales_order_item_product = sales_order_item_product
        #                         , sales_order_item_product_foreign_key = '1'
        #                         , sales_order_item_terms = sales_order_item_terms
        #                         , sales_order_item_order_item = sales_order_item_order_item
        #                         , sales_order_item_po = sales_order_item_po
        #                         # , sales_order_item_customer_id = sales_order_item_customer_id
        #                         , sales_order_item_customer_id_foreign_key = '1' #sales_order_item_customer_id_foreign_key
        #                         # , sales_order_item_customer_name = sales_order_item_customer_name
        #                         , sales_order_item_sidemark = sales_order_item_sidemark
        #                         , sales_order_item_entered = sales_order_item_entered
        #                         , sales_order_item_credit_ok = sales_order_item_credit_ok
        #                         , sales_order_item_printed = sales_order_item_printed
        #                         , sales_order_item_labels = sales_order_item_labels
        #                         , sales_order_item_packed = sales_order_item_packed
        #                         , sales_order_item_shipped_date = sales_order_item_shipped_date
        #                         , sales_order_item_required = sales_order_item_required
        #                         , sales_order_item_canceled = sales_order_item_canceled
        #                         , sales_order_item_model = sales_order_item_model
        #                         # , sales_order_item_color_style = sales_order_item_color_style
        #                         , sales_order_item_color_foreign_key = sales_order_item_color_foreign_key
        #                         , sales_order_item_width = sales_order_item_width
        #                         , sales_order_item_height = sales_order_item_height
        #                         , sales_order_item_ordered = sales_order_item_ordered
        #                         , sales_order_item_shipped_quantity = sales_order_item_shipped_quantity
        #                         , sales_order_item_net_sale = sales_order_item_net_sale
        #                         , sales_order_item_cost_of_good_sold = sales_order_item_cost_of_good_sold
                                
                        
        #                         , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason
        #                         , import_version = 'v 1.0', import_batch = 0, import_user = 'admin')

        #         #messages.success(request, 'Form successfully submitted') # Any message you wish
            
        #     else:
        #         sales_order_item_product_category = tran_sales_order_items[i].sales_order_item_product_category
        #         sales_order_item_warehouse = tran_sales_order_items[i].sales_order_item_warehouse
        #         sales_order_item_site = tran_sales_order_items[i].sales_order_item_site
        #         sales_order_item_status = tran_sales_order_items[i].sales_order_item_status
        #         sales_order_item_product = tran_sales_order_items[i].sales_order_item_product
        #         sales_order_item_product_foreign_key = '1'
        #         sales_order_item_terms = tran_sales_order_items[i].sales_order_item_terms
        #         sales_order_item_order_item = tran_sales_order_items[i].sales_order_item_order_item
        #         sales_order_item_po = tran_sales_order_items[i].sales_order_item_po
        #         sales_order_item_customer_id = tran_sales_order_items[i].sales_order_item_customer_id
        #         sales_order_item_customer_id_foreign_key = '1' #tran_sales_order_items[i].sales_order_item_customer_id_foreign_key
        #         sales_order_item_customer_name = tran_sales_order_items[i].sales_order_item_customer_name
        #         sales_order_item_sidemark = tran_sales_order_items[i].sales_order_item_sidemark
        #         sales_order_item_entered = tran_sales_order_items[i].sales_order_item_entered
        #         sales_order_item_credit_ok = tran_sales_order_items[i].sales_order_item_credit_ok
        #         sales_order_item_printed = tran_sales_order_items[i].sales_order_item_printed
        #         sales_order_item_labels = tran_sales_order_items[i].sales_order_item_labels
        #         sales_order_item_packed = tran_sales_order_items[i].sales_order_item_packed
        #         sales_order_item_shipped_date = tran_sales_order_items[i].sales_order_item_shipped_date
        #         sales_order_item_required = tran_sales_order_items[i].sales_order_item_required
        #         sales_order_item_canceled = tran_sales_order_items[i].sales_order_item_canceled
        #         sales_order_item_model = tran_sales_order_items[i].sales_order_item_model
        #         sales_order_item_color_style = tran_sales_order_items[i].sales_order_item_color_style
        #         sales_order_item_color_foreign_key = tran_sales_order_items[i].sales_order_item_color_foreign_key
        #         sales_order_item_width = tran_sales_order_items[i].sales_order_item_width
        #         sales_order_item_height = tran_sales_order_items[i].sales_order_item_height
        #         sales_order_item_ordered = tran_sales_order_items[i].sales_order_item_ordered
        #         sales_order_item_shipped_quantity = tran_sales_order_items[i].sales_order_item_shipped_quantity
        #         sales_order_item_net_sale = tran_sales_order_items[i].sales_order_item_net_sale
        #         sales_order_item_cost_of_good_sold = tran_sales_order_items[i].sales_order_item_cost_of_good_sold
                
        #         row_is_current = tran_sales_order_items[i].row_is_current
        #         row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #         row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #         row_change_reason = "original state"

        #         fact_sales_order_item = Fact_sales_order_item(
        #                                   sales_order_item_product_category=sales_order_item_product_category
        #                                 , sales_order_item_warehouse=sales_order_item_warehouse
        #                                 , sales_order_item_site= sales_order_item_site
        #                                 , sales_order_item_status = sales_order_item_status
        #                                 # , sales_order_item_product = sales_order_item_product
        #                                 , sales_order_item_product_foreign_key = sales_order_item_product_foreign_key
        #                                 , sales_order_item_terms = sales_order_item_terms
        #                                 , sales_order_item_order_item = sales_order_item_order_item
        #                                 , sales_order_item_po = sales_order_item_po
        #                                 # , sales_order_item_customer_id = sales_order_item_customer_id
        #                                 , sales_order_item_customer_id_foreign_key = sales_order_item_customer_id_foreign_key
        #                                 # , sales_order_item_customer_name = sales_order_item_customer_name
        #                                 , sales_order_item_sidemark = sales_order_item_sidemark
        #                                 , sales_order_item_entered = sales_order_item_entered
        #                                 , sales_order_item_credit_ok = sales_order_item_credit_ok
        #                                 , sales_order_item_printed = sales_order_item_printed
        #                                 , sales_order_item_labels = sales_order_item_labels
        #                                 , sales_order_item_packed = sales_order_item_packed
        #                                 , sales_order_item_shipped_date = sales_order_item_shipped_date
        #                                 , sales_order_item_required = sales_order_item_required
        #                                 , sales_order_item_canceled = sales_order_item_canceled
        #                                 , sales_order_item_model = sales_order_item_model
        #                                 # , sales_order_item_color_style = sales_order_item_color_style
        #                                 , sales_order_item_color_foreign_key = sales_order_item_color_foreign_key
        #                                 , sales_order_item_width = sales_order_item_width
        #                                 , sales_order_item_height = sales_order_item_height
        #                                 , sales_order_item_ordered = sales_order_item_ordered
        #                                 , sales_order_item_shipped_quantity = sales_order_item_shipped_quantity
        #                                 , sales_order_item_net_sale = sales_order_item_net_sale
        #                                 , sales_order_item_cost_of_good_sold = sales_order_item_cost_of_good_sold
                                                                    
        #                                 , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
        #                                 , row_change_reason = row_change_reason, import_version = 'v 1.0'
        #                                 , import_batch = 0
        #                                 , import_user = 'admin'
        #                                 )
        #         fact_sales_order_item.save() 
        #         #messages.success(request, 'Form successfully submitted') # Any message you wish
        #         #print(str(len(dim_sales_order_items))+' fact_sales_order_item update successful')

 #------------------------------------------------------------------------------------------------------





            # from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product_group") 

    # post import ----------------------------------------------------------------------------------------------------------------------------------
    number_of_records_imported = Fact_sales_order_item.objects.count()
    last_import_time = Fact_sales_order_item.objects.extra(order_by = ['row_end_date'])

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
             
    
    # #print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_color")
    return render(request, 'fact_sales_order_item_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

