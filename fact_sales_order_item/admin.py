from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stage_sales_order_item
from .models import Tran_sales_order_item
from .models import Fact_sales_order_item

@admin.register(Stage_sales_order_item)
class Stage_sales_order_item_admin(ImportExportModelAdmin):
    list_display = (  'sales_order_item_product_category'
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

                                    
                  )


@admin.register(Tran_sales_order_item)
class Tran_sales_order_item_admin(ImportExportModelAdmin):
    list_display = (  'sales_order_item_product_category'
                    , 'sales_order_item_warehouse'
                    , 'sales_order_item_site'
                    , 'sales_order_item_status'
                    , 'sales_order_item_product'
                    , 'sales_order_item_product_foreign_key'
                    , 'sales_order_item_terms'
                    , 'sales_order_item_order_item'
                    , 'sales_order_item_po'
                    , 'sales_order_item_customer_id'
                    , 'sales_order_item_customer_id_foreign_key'
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
                    , 'sales_order_item_color_foreign_key'
                    , 'sales_order_item_width'
                    , 'sales_order_item_height'
                    , 'sales_order_item_ordered'
                    , 'sales_order_item_shipped_quantity'
                    , 'sales_order_item_net_sale'
                    , 'sales_order_item_cost_of_good_sold'

                    , 'row_is_current', 'row_start_date'
                    , 'row_end_date', 'row_change_reason')


@admin.register(Fact_sales_order_item)
class Fact_sales_order_item_admin(ImportExportModelAdmin):
    list_display = (  'sales_order_item_key'
                    , 'sales_order_item_product_category'
                    , 'sales_order_item_warehouse'
                    , 'sales_order_item_site'
                    , 'sales_order_item_status'
                    , 'sales_order_item_product_foreign_key'
                    , 'sales_order_item_terms'
                    , 'sales_order_item_order_item'
                    , 'sales_order_item_po'
                    , 'sales_order_item_customer_id_foreign_key'
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
                    , 'sales_order_item_width'
                    , 'sales_order_item_height'
                    , 'sales_order_item_ordered'
                    , 'sales_order_item_shipped_quantity'
                    , 'sales_order_item_net_sale'
                    , 'sales_order_item_cost_of_good_sold'


                    , 'row_is_current', 'row_start_date'
                    , 'row_end_date', 'row_change_reason'
                    , 'import_version', 'import_batch', 'import_user')
