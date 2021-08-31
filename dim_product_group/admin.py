from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stage_product_group
from .models import Tran_product_group
from .models import Dim_product_group

 
@admin.register(Stage_product_group)
class Stage_product_admin(ImportExportModelAdmin):
    list_display = ('product_group','product_group_description', 'product', 'product_description', 'product_type'
                  , 'dealer', 'oe')


@admin.register(Tran_product_group)
class Tran_product_admin(ImportExportModelAdmin):
    list_display = ('product_group','product_group_description', 'product', 'product_description', 'product_type'
                  , 'dealer', 'oe'
                  
                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason')


@admin.register(Dim_product_group)
class Dim_product_admin(ImportExportModelAdmin):
    list_display = ('product_group','product_group_description', 'product', 'product_description', 'product_type'
                  , 'dealer', 'oe'
                  
                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason')
