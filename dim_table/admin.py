from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Dim_table


@admin.register(Dim_table)
class Dim_tableAdmin(ImportExportModelAdmin):
    list_display = ('table_name', 'last_batch_imported', 'number_of_records_imported', 'last_import_version'
                  , 'last_import_user', 'row_is_current', 'row_start_date', 'row_end_date', 'row_change_reason')