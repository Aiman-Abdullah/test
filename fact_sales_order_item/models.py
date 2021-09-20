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

class Stage_sales_order_item(models.Model):    

    sales_order_item_product_category = models.CharField(max_length=100, null=False)
    sales_order_item_warehouse = models.CharField(max_length=100, null=True)
    sales_order_item_site = models.CharField(max_length=100, null=True)
    sales_order_item_status = models.CharField(max_length=100, null=True)
    sales_order_item_product = models.CharField(max_length=100, null=False)
    sales_order_item_terms = models.CharField(max_length=100, null=True)
    sales_order_item_order_item = models.CharField(max_length=100, null=False, primary_key=True) # primary key
    sales_order_item_po = models.CharField(max_length=100, null=True)
    sales_order_item_customer_id = models.CharField(max_length=100, null=True)
    sales_order_item_customer_name = models.CharField(max_length=100, null=True)
    sales_order_item_sidemark = models.CharField(max_length=100, null=True)
    sales_order_item_entered = models.CharField(max_length=100, null=True)
    sales_order_item_credit_ok = models.CharField(max_length=100, null=True)
    sales_order_item_printed = models.CharField(max_length=100, null=True)
    sales_order_item_labels = models.CharField(max_length=100, null=True)
    sales_order_item_packed = models.CharField(max_length=100, null=True)
    sales_order_item_shipped_date = models.CharField(max_length=100, null=True)
    sales_order_item_required = models.CharField(max_length=100, null=True)
    sales_order_item_canceled = models.CharField(max_length=100, null=True)
    sales_order_item_model = models.CharField(max_length=100, null=True)
    sales_order_item_color_style = models.CharField(max_length=100, null=True)
    sales_order_item_width = models.CharField(max_length=100, null=True)
    sales_order_item_height = models.CharField(max_length=100, null=True)
    sales_order_item_ordered = models.CharField(max_length=100, null=True)
    sales_order_item_shipped_quantity = models.CharField(max_length=100, null=True)
    sales_order_item_net_sale = models.CharField(max_length=100, null=True)
    sales_order_item_cost_of_good_sold = models.CharField(max_length=100, null=True)

    class Meta:
        managed = False

        db_table = 'jcwf_stage_sales_order_item'

    def __str__(self):
      return self.sales_order_item_order_item


class Tran_sales_order_item(models.Model):

    sales_order_item_product_category = models.CharField(max_length=100, null=False)
    sales_order_item_warehouse = models.CharField(max_length=100, null=True)
    sales_order_item_site = models.CharField(max_length=100, null=True)
    sales_order_item_status = models.CharField(max_length=100, null=True)
    sales_order_item_product = models.CharField(max_length=100, null=False)
    sales_order_item_product_foreign_key = models.CharField(max_length=100, null=True) #models.IntegerField()
    sales_order_item_terms = models.CharField(max_length=100, null=True)
    sales_order_item_order_item = models.CharField(max_length=100, null=False, primary_key=True) # primary key
    sales_order_item_po = models.CharField(max_length=100, null=True)
    sales_order_item_customer_id = models.CharField(max_length=100, null=True)
    sales_order_item_customer_id_foreign_key = models.CharField(max_length=100, null=True) #models.IntegerField()
    sales_order_item_customer_name = models.CharField(max_length=100, null=True)
    sales_order_item_sidemark = models.CharField(max_length=100, null=True)
    sales_order_item_entered = models.CharField(max_length=100, null=True)
    sales_order_item_credit_ok = models.CharField(max_length=100, null=True)
    sales_order_item_printed = models.CharField(max_length=100, null=True)
    sales_order_item_labels = models.CharField(max_length=100, null=True)
    sales_order_item_packed = models.CharField(max_length=100, null=True)
    sales_order_item_shipped_date = models.CharField(max_length=100, null=True)
    sales_order_item_required = models.CharField(max_length=100, null=True)
    sales_order_item_canceled = models.CharField(max_length=100, null=True)
    sales_order_item_model = models.CharField(max_length=100, null=True)
    sales_order_item_color_style = models.CharField(max_length=100, null=True)
    sales_order_item_color_foreign_key = models.CharField(max_length=100, null=True) #models.IntegerField()
    sales_order_item_width = models.CharField(max_length=100, null=True)
    sales_order_item_height = models.CharField(max_length=100, null=True)
    sales_order_item_ordered = models.CharField(max_length=100, null=True)
    sales_order_item_shipped_quantity = models.CharField(max_length=100, null=True)
    sales_order_item_net_sale = models.CharField(max_length=100, null=True)
    sales_order_item_cost_of_good_sold = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_tran_sales_order_item'

    def __str__(self):
        return self.sales_order_item_order_item


class Fact_sales_order_item(models.Model):

    sales_order_item_key = models.AutoField(primary_key=True)

    sales_order_item_product_category = models.CharField(max_length=100, null=False)
    sales_order_item_warehouse = models.CharField(max_length=100, null=True)
    sales_order_item_site = models.CharField(max_length=100, null=True)
    sales_order_item_status = models.CharField(max_length=100, null=True)


    sales_order_item_product_foreign_key = models.CharField(max_length=100, null=True)

    # sales_order_item_product_foreign_key = models.ForeignKey(
    #     'dim_product.Dim_product',
    #     on_delete=models.PROTECT,
    # )

    sales_order_item_terms = models.CharField(max_length=100, null=True)
    sales_order_item_order_item = models.CharField(max_length=100, null=True)
    sales_order_item_po = models.CharField(max_length=100, null=True)

    sales_order_item_customer_id_foreign_key = models.CharField(max_length=100, null=True)
   
    # sales_order_item_customer_id_foreign_key = models.ForeignKey(
    #     'dim_customer.Dim_customer',
    #     on_delete=models.PROTECT,
    # )

    sales_order_item_sidemark = models.CharField(max_length=100, null=True)
    sales_order_item_entered = models.CharField(max_length=100, null=True)
    sales_order_item_credit_ok = models.CharField(max_length=100, null=True)
    sales_order_item_printed = models.CharField(max_length=100, null=True)
    sales_order_item_labels = models.CharField(max_length=100, null=True)
    sales_order_item_packed = models.CharField(max_length=100, null=True)
    sales_order_item_shipped_date = models.CharField(max_length=100, null=True)
    sales_order_item_required = models.CharField(max_length=100, null=True)
    sales_order_item_canceled = models.CharField(max_length=100, null=True)
    sales_order_item_model = models.CharField(max_length=100, null=True)

    sales_order_item_color_foreign_key = models.CharField(max_length=100, null=True)

    # sales_order_item_color_foreign_key = models.ForeignKey(
    #     'dim_color.Dim_color',
    #     on_delete=models.PROTECT,
    # )

    sales_order_item_width = models.CharField(max_length=100, null=True)
    sales_order_item_height = models.CharField(max_length=100, null=True)
    sales_order_item_ordered = models.CharField(max_length=100, null=True)
    sales_order_item_shipped_quantity = models.CharField(max_length=100, null=True)
    sales_order_item_net_sale = models.CharField(max_length=100, null=True)
    sales_order_item_cost_of_good_sold = models.CharField(max_length=100, null=True)

    row_is_current  = models.CharField(max_length=100, null=False)
    row_start_date  = models.DateTimeField()
    row_end_date  = models.DateTimeField()
    row_change_reason = models.CharField(max_length=100, null=False)
    import_version = models.CharField(max_length=100, null=False)
    import_batch = models.CharField(max_length=100, null=False)
    import_user = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'jcwf_fact_sales_order_item'

    def __str__(self):
        return self.sales_order_item_order_item
