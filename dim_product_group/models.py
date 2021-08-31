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

class Stage_product_group(models.Model):    
    product_group = models.CharField(max_length=100, null=False, primary_key=True)
    product_group_description = models.CharField(max_length=100, null=False)
    product = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100, null=False)
    product_type = models.CharField(max_length=100, null=False)
    dealer = models.CharField(max_length=100, null=True)
    oe = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False

        db_table = 'jcwf_stage_product_group'

    def __str__(self):
      return self.product_group


class Tran_product_group(models.Model):
    product_group = models.CharField(max_length=100, null=False, primary_key=True)
    product_group_description = models.CharField(max_length=100, null=False)
    product = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100, null=False)
    product_type = models.CharField(max_length=100, null=False)
    dealer = models.CharField(max_length=100, null=True)
    oe = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_tran_product_group'

    def __str__(self):
        return self.product_group


class Dim_product_group(models.Model):
    product_group_key = models.AutoField(primary_key=True)
    product_group = models.CharField(max_length=100, null=False)
    product_group_description = models.CharField(max_length=100, null=False)
    product = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100, null=False)
    product_type = models.CharField(max_length=100, null=False)
    dealer = models.CharField(max_length=100, null=True)
    oe = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)
    import_version = models.CharField(max_length=100, null=False)
    import_batch = models.CharField(max_length=100, null=False)
    import_user = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_dim_product_group'

    def __str__(self):
        return self.product_group
