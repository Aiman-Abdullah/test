from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stage_discount
from .models import Tran_discount
from .models import Dim_discount

@admin.register(Stage_discount)
class Stage_discount_admin(ImportExportModelAdmin):
    list_display = ('discount_customer_id'
                    , 'discount_customer_name'
                    , 'discount_account_type'
                    , 'discount_product_id'
                    , 'discount_product_name'
                    , 'discount_product_discount_category'
                    , 'discount_model'
                    , 'discount_color'
                    , 'discount_discount_group'
                    , 'discount_discount_from'
                    , 'discount_discount_to'
                    , 'discount_eff'
                    , 'discount_factor'                                    
                  )


@admin.register(Tran_discount)
class Tran_discount_admin(ImportExportModelAdmin):
    list_display = (  'discount_name'
                    , 'discount_customer_id'
                    , 'discount_customer_name'
                    , 'discount_account_type'
                    , 'discount_product_id'
                    , 'discount_product_name'
                    , 'discount_product_discount_category'
                    , 'discount_model'
                    , 'discount_color'
                    , 'discount_discount_group'
                    , 'discount_discount_from'
                    , 'discount_discount_to'
                    , 'discount_eff'
                    , 'discount_factor'

                    , 'row_is_current', 'row_start_date'
                    , 'row_end_date', 'row_change_reason')


@admin.register(Dim_discount)
class Dim_discount_admin(ImportExportModelAdmin):
    list_display = (  'discount_key'
                    , 'discount_name'
                    , 'discount_customer_id'
                    , 'discount_customer_name'
                    , 'discount_account_type'
                    , 'discount_product_id'
                    , 'discount_product_name'
                    , 'discount_product_discount_category'
                    , 'discount_model'
                    , 'discount_color'
                    , 'discount_discount_group'
                    , 'discount_discount_from'
                    , 'discount_discount_to'
                    , 'discount_eff'
                    , 'discount_factor'

                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason'
                  , 'import_version', 'import_batch', 'import_user')
