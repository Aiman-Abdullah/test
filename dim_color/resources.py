from import_export import resources
from .models import Stage_color  
from .models import Tran_color 
from .models import Dim_color 

class Stage_color_resource(resources.ModelResource):
    class meta:
        model = Stage_color

class Tran_color_resource(resources.ModelResource):
    class meta:
        model = Tran_color

class Dim_color_resource(resources.ModelResource):
    class meta:
        model = Dim_color
        