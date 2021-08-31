from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import dimAudit

@admin.register(dimAudit)
class dimAuditAdmin(ImportExportModelAdmin):
    list_display = ('productid','description')