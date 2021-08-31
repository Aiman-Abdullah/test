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

class Stage_color(models.Model):    
    color_temp_key = models.CharField(max_length=100, null=False, primary_key=True)
    color_table = models.CharField(max_length=100, null=False)
    color_group = models.CharField(max_length=100, null=True)
    color_name = models.CharField(max_length=100, null=True)
    color_description = models.CharField(max_length=100, null=True)
    color_bo_date = models.CharField(max_length=100, null=False)
    color_disc_group = models.CharField(max_length=100, null=True)
    color_formula_group = models.CharField(max_length=100, null=True)
    color_begin_date = models.CharField(max_length=100, null=True)
    color_discontinued_date = models.CharField(max_length=100, null=True)
    color_inactive_date = models.CharField(max_length=100, null=True)
    color_constants = models.CharField(max_length=100, null=True)
    

    class Meta:
        managed = False

        db_table = 'jcwf_stage_color'

    def __str__(self):
      return self.color_table


class Tran_color(models.Model):
    color_temp_key = models.CharField(max_length=100, null=False, primary_key=True)
    color_table = models.CharField(max_length=100, null=False)
    color_group = models.CharField(max_length=100, null=True)
    color_name = models.CharField(max_length=100, null=True)
    color_description = models.CharField(max_length=100, null=True)
    color_bo_date = models.CharField(max_length=100, null=False)
    color_disc_group = models.CharField(max_length=100, null=True)
    color_formula_group = models.CharField(max_length=100, null=True)
    color_begin_date = models.CharField(max_length=100, null=True)
    color_discontinued_date = models.CharField(max_length=100, null=True)
    color_inactive_date = models.CharField(max_length=100, null=True)
    color_constants = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_tran_color'

    def __str__(self):
        return self.color_temp_key


class Dim_color(models.Model):

    color_key = models.AutoField(primary_key=True)

    color_unique_key = models.CharField(max_length=100, null=False)
    color_table = models.CharField(max_length=100, null=False)
    color_group = models.CharField(max_length=100, null=True)
    color_name = models.CharField(max_length=100, null=True)
    color_description = models.CharField(max_length=100, null=True)
    color_bo_date = models.CharField(max_length=100, null=False)
    color_disc_group = models.CharField(max_length=100, null=True)
    color_formula_group = models.CharField(max_length=100, null=True)
    color_begin_date = models.CharField(max_length=100, null=True)
    color_discontinued_date = models.CharField(max_length=100, null=True)
    color_inactive_date = models.CharField(max_length=100, null=True)
    color_constants = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)
    import_version = models.CharField(max_length=100, null=False)
    import_batch = models.CharField(max_length=100, null=False)
    import_user = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_dim_color'

    def __str__(self):
        return self.customer_key
