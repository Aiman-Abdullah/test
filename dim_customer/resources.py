from import_export import resources
from .models import Stage_customer  
from .models import Tran_customer 
from .models import Dim_customer 

class Stage_customer_resource(resources.ModelResource):
    class meta:
        model = Stage_customer

class Tran_customer_resource(resources.ModelResource):
    class meta:
        model = Tran_customer

class Dim_customer_resource(resources.ModelResource):
    class meta:
        model = Dim_customer
        