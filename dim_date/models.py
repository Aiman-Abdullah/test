from django.db import models

# model types for reference
# models.CharField(max_length=100, null=False, primary_key=True)
# models.CharField(max_length=100, null=False)
# models.CharField(max_length=100)
# models.FloatField(max_digits=16, decimal_places=4)
# models.DateTimeField()
# models.ForeignKey(__name__, on_delete=models.CASCADE)
# models.TextField(max_length =500)

# models.ManyToManyField("self")
# models.OneToOneField()

# models.DateField() # I don't use often 
# models.IntegerField()
# models.AutoField() # An IntegerField that automatically increments according to available IDs.
# models.BinaryField() 
# models.BooleanField()
# models.DecimalField(max_digits=16, decimal_places=4)
# models.FloatField(max_digits=16, decimal_places=4)
# models.ImageField(max_digits=16, decimal_places=4)
# models.JSONField(max_digits=16, decimal_places=4)

# Create your models here.

class Stage_date(models.Model):
    date_date_key = models.CharField(max_length=100, null=False, primary_key=True)
    date_date_name = models.DateTimeField()
    date_full_date_usa = models.CharField(max_length=100)
    date_day_of_week = models.CharField(max_length=100, null=True)
    date_day_name = models.CharField(max_length=100, null=False)
    date_day_of_month = models.CharField(max_length=100, null=True)
    date_day_of_year = models.CharField(max_length=100, null=True)
    date_week_of_year = models.CharField(max_length=100, null=True)
    date_month_name = models.CharField(max_length=100, null=True)
    date_month_of_year = models.CharField(max_length=100, null=True)
    date_quarter = models.CharField(max_length=100, null=True)
    date_quarter_name = models.CharField(max_length=100, null=True)
    date_year_name = models.CharField(max_length=100, null=True)
    date_is_weekday = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False
        db_table = 'jcwf_stage_date'

    def __str__(self):
        return self.customer_account


class Dim_date(models.Model):
    date_date_key = models.CharField(max_length=100, null=False, primary_key=True)
    date_date_name = models.DateTimeField()
    date_full_date_usa = models.CharField(max_length=100)
    date_day_of_week = models.CharField(max_length=100, null=True)
    date_day_name = models.CharField(max_length=100, null=False)
    date_day_of_month = models.CharField(max_length=100, null=True)
    date_day_of_year = models.CharField(max_length=100, null=True)
    date_week_of_year = models.CharField(max_length=100, null=True)
    date_month_name = models.CharField(max_length=100, null=True)
    date_month_of_year = models.CharField(max_length=100, null=True)
    date_quarter = models.CharField(max_length=100, null=True)
    date_quarter_name = models.CharField(max_length=100, null=True)
    date_year_name = models.CharField(max_length=100, null=True)
    date_is_weekday = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)
    import_version  = models.CharField(max_length=100, null=False)
    import_batch  = models.CharField(max_length=100, null=False)
    import_user = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_dim_date'

    def __str__(self):
        return self.customer_account