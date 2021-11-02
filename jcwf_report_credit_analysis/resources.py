from import_export import resources
from .models import Stage_product  
from .models import Tran_product 
from .models import Dim_product 

class Stage_product_resource(resources.ModelResource):
    class meta:
        model = Stage_product

class Tran_product_resource(resources.ModelResource):
    class meta:
        model = Tran_product

class Dim_product_resource(resources.ModelResource):
    class meta:
        model = Dim_product