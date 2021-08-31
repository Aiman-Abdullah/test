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

class Stage_discount(models.Model):    
    discount_customer_id = models.CharField(max_length=100, null=False, primary_key=True)
    discount_customer_name = models.CharField(max_length=100, null=True)
    discount_account_type = models.CharField(max_length=100, null=True)
    discount_product_id = models.CharField(max_length=100, null=True)
    discount_product_name = models.CharField(max_length=100, null=True)
    discount_product_discount_category = models.CharField(max_length=100, null=True)
    discount_model = models.CharField(max_length=100, null=True)
    discount_color = models.CharField(max_length=100, null=True)
    discount_discount_group = models.CharField(max_length=100, null=True)
    discount_discount_from = models.CharField(max_length=100, null=True)
    discount_discount_to = models.CharField(max_length=100, null=True)
    discount_eff = models.CharField(max_length=100, null=True)
    discount_factor = models.CharField(max_length=100, null=True)    

    class Meta:
        managed = False

        db_table = 'jcwf_stage_discount'

    def __str__(self):
      return self.discount_customer_id


class Tran_discount(models.Model):
    discount_name = models.CharField(max_length=100, null=False, primary_key=True)
    discount_customer_id = models.CharField(max_length=100, null=False)
    discount_customer_name = models.CharField(max_length=100, null=True)
    discount_account_type = models.CharField(max_length=100, null=True)
    discount_product_id = models.CharField(max_length=100, null=True)
    discount_product_name = models.CharField(max_length=100, null=True)
    discount_product_discount_category = models.CharField(max_length=100, null=True)
    discount_model = models.CharField(max_length=100, null=True)
    discount_color = models.CharField(max_length=100, null=True)
    discount_discount_group = models.CharField(max_length=100, null=True)
    discount_discount_from = models.CharField(max_length=100, null=True)
    discount_discount_to = models.CharField(max_length=100, null=True)
    discount_eff = models.CharField(max_length=100, null=True)
    discount_factor = models.CharField(max_length=100, null=True)   

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_tran_discount'

    def __str__(self):
        return self.discount_name


class Dim_discount(models.Model):

    discount_key = models.AutoField(primary_key=True)

    discount_name = models.CharField(max_length=100, null=True)
    discount_customer_id = models.CharField(max_length=100, null=True)
    discount_customer_name = models.CharField(max_length=100, null=True)
    discount_account_type = models.CharField(max_length=100, null=True)
    discount_product_id = models.CharField(max_length=100, null=True)
    discount_product_name = models.CharField(max_length=100, null=True)
    discount_product_discount_category = models.CharField(max_length=100, null=True)
    discount_model = models.CharField(max_length=100, null=True)
    discount_color = models.CharField(max_length=100, null=True)
    discount_discount_group = models.CharField(max_length=100, null=True)
    discount_discount_from = models.CharField(max_length=100, null=True)
    discount_discount_to = models.CharField(max_length=100, null=True)
    discount_eff = models.CharField(max_length=100, null=True)
    discount_factor = models.CharField(max_length=100, null=True)   

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)
    import_version = models.CharField(max_length=100, null=False)
    import_batch = models.CharField(max_length=100, null=False)
    import_user = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_dim_discount'

    def __str__(self):
        return self.discount_name
