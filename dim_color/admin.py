from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stage_color
from .models import Tran_color
from .models import Dim_color

@admin.register(Stage_color)
class Stage_color_admin(ImportExportModelAdmin):
    list_display = ('color_temp_key'
                    , 'color_table'
                    , 'color_group'
                    , 'color_name'
                    , 'color_description'
                    , 'color_bo_date'
                    , 'color_disc_group'
                    , 'color_formula_group'
                    , 'color_begin_date'
                    , 'color_discontinued_date'
                    , 'color_inactive_date'
                    , 'color_constants'
                                    
                  )


@admin.register(Tran_color)
class Tran_color_admin(ImportExportModelAdmin):
    list_display = (  'color_temp_key'
                    , 'color_table'
                    , 'color_group'
                    , 'color_name'
                    , 'color_description'
                    , 'color_bo_date'
                    , 'color_disc_group'
                    , 'color_formula_group'
                    , 'color_begin_date'
                    , 'color_discontinued_date'
                    , 'color_inactive_date'
                    , 'color_constants'

                    , 'row_is_current', 'row_start_date'
                    , 'row_end_date', 'row_change_reason')


@admin.register(Dim_color)
class Dim_color_admin(ImportExportModelAdmin):
    list_display = (  'color_key'
                    , 'color_unique_key'
                    , 'color_table'
                    , 'color_group'
                    , 'color_name'
                    , 'color_description'
                    , 'color_bo_date'
                    , 'color_disc_group'
                    , 'color_formula_group'
                    , 'color_begin_date'
                    , 'color_discontinued_date'
                    , 'color_inactive_date'
                    , 'color_constants'

                  , 'row_is_current', 'row_start_date'
                  , 'row_end_date', 'row_change_reason'
                  , 'import_version', 'import_batch', 'import_user')
