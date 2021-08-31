from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Dim_date, Stage_date

 
@admin.register(Stage_date)
class Stage_date_admin(ImportExportModelAdmin):
    list_display = ('date_date_key'
                    ,'date_date_name'
                    , 'date_full_date_usa'
                    , 'date_day_of_week'
                    , 'date_day_name'
                    , 'date_day_of_month'
                    , 'date_day_of_year'
                    , 'date_week_of_year'
                    , 'date_month_name'
                    , 'date_month_of_year'
                    , 'date_quarter'
                    , 'date_quarter_name'
                    , 'date_year_name'
                    , 'date_is_weekday'
                    )

@admin.register(Dim_date)
class Dim_date_admin(ImportExportModelAdmin):
    list_display = ('date_date_key'
                    ,'date_date_name'
                    , 'date_full_date_usa'
                    , 'date_day_of_week'
                    , 'date_day_name'
                    , 'date_day_of_month'
                    , 'date_day_of_year'
                    , 'date_week_of_year'
                    , 'date_month_name'
                    , 'date_month_of_year'
                    , 'date_quarter'
                    , 'date_quarter_name'
                    , 'date_year_name'
                    , 'date_is_weekday'

                    , 'row_is_current', 'row_start_date'
                    , 'row_end_date', 'row_change_reason'
                    , 'import_version', 'import_batch', 'import_user'
                    )
