from import_export import resources
from .models import Stage_sales_order_item  
from .models import Tran_sales_order_item 
from .models import Fact_sales_order_item 

class Stage_sales_order_item_resource(resources.ModelResource):
    class meta:
        model = Stage_sales_order_item

class Tran_sales_order_item_resource(resources.ModelResource):
    class meta:
        model = Tran_sales_order_item

class Fact_sales_order_item_resource(resources.ModelResource):
    class meta:
        model = Fact_sales_order_item
        