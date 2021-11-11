import psycopg2
import pandas as pd
from pandas import DataFrame
import datetime as dt

# writing query

def customer_foreign_key_query(Customer_Name):
    # if len(Customer_Name)>1:
    Customer_Name = str('\'')+str(Customer_Name)+str('\'')
    
    customer_filter = (str("""
    DROP TABLE IF EXISTS  jcwf_temp_table_customer_foreign_key_look_up;
    SELECT customer_key INTO TABLE jcwf_temp_table_customer_foreign_key_look_up FROM jcwf_dim_customer WHERE customer_name = """)
    +
    str(Customer_Name)
    +
    str(""";""")
        +
    str("""SELECT * FROM jcwf_temp_table_customer_foreign_key_look_up;""")
    )
    # print(customer_filter)

    conn = psycopg2.connect("host='econometricdatasolutionsdb.postgres.database.azure.com' dbname=postgres user='Christopher@econometricdatasolutionsdb' password='Darkknight17!'")
    cur = conn.cursor()
    cur.execute(customer_filter) 
    rows = cur.fetchall()

    df = DataFrame(rows,columns=[
        'sales_order_item_status'  
     ])
    # print(df.iloc[0]['sales_order_item_status']) 

    conn.commit()
    conn.close()
    return(df.iloc[0]['sales_order_item_status'])