from import_export import resources
from .models import Stage_discount  
from .models import Tran_discount 
from .models import Dim_discount 

class Stage_discount_resource(resources.ModelResource):
    class meta:
        model = Stage_discount

class Tran_discount_resource(resources.ModelResource):
    class meta:
        model = Tran_discount

class Dim_discount_resource(resources.ModelResource):
    class meta:
        model = Dim_discount
        