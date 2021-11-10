import psycopg2
import pandas as pd
from pandas import DataFrame
import datetime as dt

# writing query

def report_query(customer_key, start_date, end_date):
    start_date = str('\'')+start_date+str('\'')
    end_date = str('\'')+end_date+str('\'')
    if len(customer_key)>1:
        customer_filter = (str("""
        DROP TABLE IF EXISTS  jcwf_temp_table_t;
        SELECT * INTO TABLE jcwf_temp_table_t FROM jcwf_temp_table WHERE sales_order_item_customer_id_foreign_key = """)
        +
        str(customer_key)
        +
        str(""";"""))
    else:
        customer_filter =str("""
        DROP TABLE IF EXISTS  jcwf_temp_table_t;
        SELECT * INTO TABLE jcwf_temp_table_t FROM jcwf_temp_table;""")

    query = (
    str("""

    --This is a query that creates a tempeorary table of the Detail line items data, enriched with  product data and color data
    --Author: Christopher Gonzalez
    --SELECT * FROM jcwf_tran_sales_order_item

    DROP TABLE IF EXISTS  jcwf_temp_table;

    SELECT

    sales_order_item_status 
    , sales_order_item_product_foreign_key 
    , product_description
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

    INTO TABLE jcwf_temp_table
    FROM jcwf_fact_sales_order_item
    JOIN jcwf_dim_product
    ON jcwf_fact_sales_order_item.sales_order_item_product_foreign_key = jcwf_dim_product.product_key
    """)
    +
    str(
    """
    WHERE sales_order_item_entered >= 
    """)
    +
    str(start_date)
    +
    str(
    """
    AND sales_order_item_entered <=
    """)
    +
    str(end_date)
    # +
    # """
    # AND sales_order_item_customer_id_foreign_key == ""
    # """
    +
    str(""";""")
    +
    # str("""SELECT * FROM jcwf_temp_table;""")
    # +
    str(customer_filter)

    # +
    # str("""
    # SELECT  * FROM jcwf_temp_table_t;
    # """)
    +
    str("""
    DROP TABLE IF EXISTS  jcwf_temp_table_2;

    SELECT  

    sales_order_item_status 
    , sales_order_item_product_foreign_key 
    , product_description
    , sales_order_item_terms 
    , sales_order_item_order_item  
    , sales_order_item_po 
    , sales_order_item_customer_id_foreign_key 
    , Customer_Account
    , Customer_Name
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

    INTO TABLE jcwf_temp_table_2
    FROM jcwf_temp_table_t
    JOIN jcwf_dim_customer
    ON jcwf_temp_table_t.sales_order_item_customer_id_foreign_key = jcwf_dim_customer.Customer_key;""")
    # +
    # str("""SELECT * FROM jcwf_temp_table_2;""")
    +
    str("""
    DROP TABLE IF EXISTS  jcwf_temp_table_3;

    SELECT  

    sales_order_item_status 
    , sales_order_item_product_foreign_key 
    , product_description
    , sales_order_item_terms 
    , sales_order_item_order_item  
    , sales_order_item_po 
    , sales_order_item_customer_id_foreign_key 
    , Customer_Account
    , Customer_Name
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
    , color_name
    , color_description
    , sales_order_item_width
    , sales_order_item_height 
    , sales_order_item_ordered
    , sales_order_item_shipped_quantity
    , sales_order_item_net_sale  

    INTO TABLE jcwf_temp_table_3
    FROM jcwf_temp_table_2
    JOIN jcwf_dim_color
    ON jcwf_temp_table_2.sales_order_item_color_foreign_key = jcwf_dim_color.color_key;""")
    +
    str("""SELECT * FROM jcwf_temp_table_3;""")
    )
    # print(query)

    # importing data from the data warehouse using psycopg2
    conn = psycopg2.connect("host='econometricdatasolutionsdb.postgres.database.azure.com' dbname=postgres user='Christopher@econometricdatasolutionsdb' password='Darkknight17!'")
    cur = conn.cursor()
    cur.execute(query) 
    rows = cur.fetchall()

    df = DataFrame(rows,columns=[
    
      'sales_order_item_status' 
    , 'sales_order_item_product_foreign_key' 
    , 'product_description'
    , 'sales_order_item_terms' 
    , 'sales_order_item_order_item'  
    , 'sales_order_item_po' 
    , 'sales_order_item_customer_id_foreign_key' 
    , 'Customer_Account'
    , 'Customer_Name'
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
    , 'sales_order_item_color_foreign_key' 
    , 'color_name'
    , 'color_description'
    , 'sales_order_item_width'
    , 'sales_order_item_height' 
    , 'sales_order_item_ordered'
    , 'sales_order_item_shipped_quantity'
    , 'sales_order_item_net_sale'  
    ])
    
    conn.commit()
    conn.close()
    return(df)

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = report_query(arg)
