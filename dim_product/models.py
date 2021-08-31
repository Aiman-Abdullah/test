from django.db import models

# Create your models here.

class Stage_product(models.Model):    
    product_id = models.CharField(max_length=100, null=False, primary_key=True)
    product_description = models.CharField(max_length=100, null=False)
    product_pdg = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, null=False)
    product_dtc = models.CharField(max_length=100, null=False)
    product_min_deposit = models.CharField(max_length=100, null=True)
    product_phase_out_date = models.CharField(max_length=100, null=True)
    product_disc_date = models.DateTimeField(max_length=100,null=True)  #DateTimeField
    product_col = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False

        db_table = 'jcwf_stage_product'

    def __str__(self):
      return self.product_id


class Tran_product(models.Model):
    product_id = models.CharField(max_length=100, null=False, primary_key=True)
    product_description = models.CharField(max_length=100, null=False)
    product_pdg = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, null=False)
    product_dtc = models.CharField(max_length=100, null=False)
    product_min_deposit = models.CharField(max_length=100, null=True)
    product_phase_out_date = models.CharField(max_length=100, null=True)
    product_disc_date = models.DateTimeField(max_length=100,null=True)  #DateTimeField
    product_discontinued = models.CharField(max_length=100, null=False)
    product_col = models.CharField(max_length=100, null=False)


    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_tran_product'

    def __str__(self):
        return self.product_id


class Dim_product(models.Model):
    product_key = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=100, null=False)
    product_description = models.CharField(max_length=100, null=False)
    product_pdg = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, null=False)
    product_dtc = models.CharField(max_length=100, null=False)
    product_min_deposit = models.CharField(max_length=100, null=True)
    product_phase_out_date = models.CharField(max_length=100, null=True)
    product_disc_date = models.CharField(max_length=100,null=True)  #DateTimeField
    product_discontinued = models.CharField(max_length=100, null=True)
    product_col = models.CharField(max_length=100, null=False)


    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)
    import_version = models.CharField(max_length=100, null=False)
    import_batch = models.CharField(max_length=100, null=False)
    import_user = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_dim_product'

    def __str__(self):
        return self.product_id
