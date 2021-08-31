from django.db import models

# Create your models here.

class Dim_table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=100, null=False)
    last_batch_imported = models.CharField(max_length=100, null=False)
    number_of_records_imported = models.CharField(max_length=100)
    last_import_version = models.CharField(max_length=100, null=False)
    last_import_user = models.CharField(max_length=100, null=False)
    row_is_current = models.CharField(max_length=100, null=True)
    row_start_date = models.CharField(max_length=100, null=True)
    row_end_date = models.CharField(max_length=100,null=True)  #DateTimeField
    row_change_reason = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False
        db_table = 'jcwf_dim_table'

    def __str__(self):
        return self.table_id
