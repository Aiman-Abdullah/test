from import_export import resources
from .models import Stage_product_group  
from .models import Tran_product_group 
from .models import Dim_product_group 

class Stage_product_group_resource(resources.ModelResource):
    class meta:
        model = Stage_product_group

class Tran_product_group_resource(resources.ModelResource):
    class meta:
        model = Tran_product_group

class Dim_product_group_resource(resources.ModelResource):
    class meta:
        model = Dim_product_group
        