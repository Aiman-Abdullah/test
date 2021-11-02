from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stage_product
from .models import Tran_product
from .models import Dim_product

 
@admin.register(Stage_product)
class Stage_product_admin(ImportExportModelAdmin):
    list_display = ('product_id','product_description', 'product_pdg', 'product_type', 'product_dtc'
                  , 'product_min_deposit', 'product_phase_out_date', 'product_disc_date', 'product_col')


@admin.register(Tran_product)
class Tran_product_admin(ImportExportModelAdmin):
    list_display = ('product_id','product_description', 'product_pdg', 'product_type', 'product_dtc'
                  , 'product_min_deposit', 'product_phase_out_date', 'product_disc_date', 'product_discontinued', 'product_col'
                  
                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason')


@admin.register(Dim_product)
class Dim_product_admin(ImportExportModelAdmin):
    list_display = ('product_id','product_description', 'product_pdg', 'product_type', 'product_dtc'
                  , 'product_min_deposit', 'product_phase_out_date', 'product_disc_date', 'product_discontinued', 'product_col'
                  
                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason')
