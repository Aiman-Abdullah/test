from import_export import resources
from .models import Dim_table 

class Dim_table_resource(resources.ModelResource):
    class meta:
        model = Dim_table