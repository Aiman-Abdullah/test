import sys
# importing libraries
import psycopg2
import pandas as pd
from pandas import DataFrame

def do_something():

    # importing data from the data warehouse using psycopg2
    conn = psycopg2.connect("host='econometricdatasolutionsdb.postgres.database.azure.com' dbname=postgres user='Christopher@econometricdatasolutionsdb' password='Darkknight17!'")
    cur = conn.cursor()
    cur.execute("""
    
    /* Updating transformation table */
    TRUNCATE jcwf_tran_sales_order_item;

    insert INTO jcwf_tran_sales_order_item (




    sales_order_item_product_category  
    , sales_order_item_warehouse  
    , sales_order_item_site 
    , sales_order_item_status 
    , sales_order_item_product 
    , sales_order_item_product_foreign_key
    , sales_order_item_terms 
    , sales_order_item_order_item  
    , sales_order_item_po  
    , sales_order_item_customer_id 
    , sales_order_item_customer_id_foreign_key
    , sales_order_item_customer_name 
    , sales_order_item_sidemark 
    , sales_order_item_entered 
    , sales_order_item_credit_ok  
    , sales_order_item_printed 
    , sales_order_item_labels 
    , sales_order_item_packed 
    , sales_order_item_shipped_date 
    , sales_order_item_required 
    , sales_order_item_canceled 
    , sales_order_item_model 
    , sales_order_item_color_style 
    , sales_order_item_width 
    , sales_order_item_height
    , sales_order_item_ordered 
    , sales_order_item_shipped_quantity 
    , sales_order_item_net_sale
    , sales_order_item_cost_of_good_sold

    )

    SELECT 

    sales_order_item_product_category  
    , sales_order_item_warehouse  
    , sales_order_item_site 
    , sales_order_item_status 
    , sales_order_item_product 
    , (SELECT product_key FROM jcwf_dim_product WHERE jcwf_dim_product.product_id = jcwf_stage_sales_order_item.sales_order_item_product) AS sales_order_item_product_foreign_key
    , sales_order_item_terms 
    , sales_order_item_order_item  
    , sales_order_item_po  
    , sales_order_item_customer_id 
    , (SELECT customer_key FROM jcwf_dim_customer WHERE jcwf_dim_customer.customer_account = jcwf_stage_sales_order_item.sales_order_item_customer_id) AS sales_order_item_customer_id_foreign_key
    , sales_order_item_customer_name 
    , sales_order_item_sidemark 
    , sales_order_item_entered 
    , sales_order_item_credit_ok  
    , sales_order_item_printed 
    , sales_order_item_labels 
    , sales_order_item_packed 
    , sales_order_item_shipped_date 
    , sales_order_item_required 
    , sales_order_item_canceled 
    , sales_order_item_model 
    , sales_order_item_color_style 
    , sales_order_item_width 
    , sales_order_item_height
    , sales_order_item_ordered 
    , sales_order_item_shipped_quantity 
    , sales_order_item_net_sale
    , sales_order_item_cost_of_good_sold

    from jcwf_stage_sales_order_item

    ON CONFLICT ON CONSTRAINT Unique_jcwf_tran_sales_order_item_id DO UPDATE set 

    sales_order_item_product_category = excluded.sales_order_item_product_category
    , sales_order_item_warehouse = excluded.sales_order_item_warehouse
    , sales_order_item_site = excluded.sales_order_item_site
    , sales_order_item_status = excluded.sales_order_item_status
    , sales_order_item_product = excluded.sales_order_item_product
    , sales_order_item_product_foreign_key = excluded.sales_order_item_product_foreign_key
    , sales_order_item_terms = excluded.sales_order_item_terms
    , sales_order_item_order_item = excluded.sales_order_item_order_item
    , sales_order_item_po = excluded.sales_order_item_po
    , sales_order_item_customer_id = excluded.sales_order_item_customer_id
    , sales_order_item_customer_name = excluded.sales_order_item_customer_name
    , sales_order_item_sidemark = excluded.sales_order_item_sidemark
    , sales_order_item_entered = excluded.sales_order_item_entered
    , sales_order_item_credit_ok = excluded.sales_order_item_credit_ok
    , sales_order_item_printed = excluded.sales_order_item_printed
    , sales_order_item_labels = excluded.sales_order_item_labels
    , sales_order_item_packed = excluded.sales_order_item_packed
    , sales_order_item_shipped_date = excluded.sales_order_item_shipped_date
    , sales_order_item_required = excluded.sales_order_item_required
    , sales_order_item_canceled = excluded.sales_order_item_canceled
    , sales_order_item_model = excluded.sales_order_item_model
    , sales_order_item_color_style = excluded.sales_order_item_color_style
    , sales_order_item_width = excluded.sales_order_item_width
    , sales_order_item_height = excluded.sales_order_item_height
    , sales_order_item_ordered = excluded.sales_order_item_ordered
    , sales_order_item_shipped_quantity = excluded.sales_order_item_shipped_quantity
    , sales_order_item_net_sale = excluded.sales_order_item_net_sale
    , sales_order_item_cost_of_good_sold = excluded.sales_order_item_cost_of_good_sold;

    -------------------------------------------------------------------------------------------------------
    /* Updating fact table */
    insert INTO jcwf_fact_sales_order_item (

    sales_order_item_product_category  
    , sales_order_item_warehouse  
    , sales_order_item_site 
    , sales_order_item_status 
    , sales_order_item_product_foreign_key
    , sales_order_item_terms 
    , sales_order_item_order_item  
    , sales_order_item_po  
    , sales_order_item_customer_id_foreign_key 
    , sales_order_item_sidemark 
    , sales_order_item_entered 
    , sales_order_item_credit_ok  
    , sales_order_item_printed 
    , sales_order_item_labels 
    , sales_order_item_packed 
    , sales_order_item_shipped_date 
    , sales_order_item_required 
    , sales_order_item_canceled 
    , sales_order_item_model 
    , sales_order_item_color_foreign_key 
    , sales_order_item_width 
    , sales_order_item_height
    , sales_order_item_ordered 
    , sales_order_item_shipped_quantity 
    , sales_order_item_net_sale
    , sales_order_item_cost_of_good_sold

    )

    SELECT 

    sales_order_item_product_category  
    , sales_order_item_warehouse  
    , sales_order_item_site 
    , sales_order_item_status 
    , sales_order_item_product_foreign_key
    , sales_order_item_terms 
    , sales_order_item_order_item  
    , sales_order_item_po  
    , sales_order_item_customer_id_foreign_key 
    , sales_order_item_sidemark 
    , sales_order_item_entered 
    , sales_order_item_credit_ok  
    , sales_order_item_printed 
    , sales_order_item_labels 
    , sales_order_item_packed 
    , sales_order_item_shipped_date 
    , sales_order_item_required 
    , sales_order_item_canceled 
    , sales_order_item_model 
    , sales_order_item_color_foreign_key 
    , sales_order_item_width 
    , sales_order_item_height
    , sales_order_item_ordered 
    , sales_order_item_shipped_quantity 
    , sales_order_item_net_sale
    , sales_order_item_cost_of_good_sold

    from jcwf_tran_sales_order_item

    ON CONFLICT ON CONSTRAINT Unique_fact_sales_order_item DO UPDATE set 

    sales_order_item_product_category = excluded.sales_order_item_product_category
    , sales_order_item_warehouse = excluded.sales_order_item_warehouse
    , sales_order_item_site = excluded.sales_order_item_site
    , sales_order_item_status = excluded.sales_order_item_status
    , sales_order_item_product_foreign_key = excluded.sales_order_item_product_foreign_key
    , sales_order_item_terms = excluded.sales_order_item_terms
    , sales_order_item_order_item = excluded.sales_order_item_order_item
    , sales_order_item_po = excluded.sales_order_item_po
    , sales_order_item_customer_id_foreign_key = excluded.sales_order_item_customer_id_foreign_key
    , sales_order_item_sidemark = excluded.sales_order_item_sidemark
    , sales_order_item_entered = excluded.sales_order_item_entered
    , sales_order_item_credit_ok = excluded.sales_order_item_credit_ok
    , sales_order_item_printed = excluded.sales_order_item_printed
    , sales_order_item_labels = excluded.sales_order_item_labels
    , sales_order_item_packed = excluded.sales_order_item_packed
    , sales_order_item_shipped_date = excluded.sales_order_item_shipped_date
    , sales_order_item_required = excluded.sales_order_item_required
    , sales_order_item_canceled = excluded.sales_order_item_canceled
    , sales_order_item_model = excluded.sales_order_item_model
    , sales_order_item_color_foreign_key = excluded.sales_order_item_color_foreign_key
    , sales_order_item_width = excluded.sales_order_item_width
    , sales_order_item_height = excluded.sales_order_item_height
    , sales_order_item_ordered = excluded.sales_order_item_ordered
    , sales_order_item_shipped_quantity = excluded.sales_order_item_shipped_quantity
    , sales_order_item_net_sale = excluded.sales_order_item_net_sale
    , sales_order_item_cost_of_good_sold = excluded.sales_order_item_cost_of_good_sold;



    """
    )


    # rows = cur.fetchall()

    # print ("\nShow me the databases:\n")
    # for row in rows:
    #     print ("   ", row)

    # df = DataFrame(rows) # ,columns=[
        
    #   'outsourceditemskey', 'outsourceditemsid', 'Status', 'Product', 'productDescription', 'terms', 'salesOrder',  'lineItem'
    # , 'customerPO', 'CustomerID', 'customername', 'Sidemark'
    # , 'Entered', 'CreditOK', 'Printed', 'Labels' , 'Packed'
    # , 'ShippedDate', 'Required', 'Canceled', 'Model', 'ClrStyle', 'colorDescription', 'WID', 'HGT', 'quantityOrdered', 'quantityShipped'
    # , 'NetSale', 'trackingStatus', 'trackingNumber', 'notes', 'updated'
        
    # ])

    conn.commit()
    conn.close()
    # df
    # return val

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = do_something(arg)

do_something()
