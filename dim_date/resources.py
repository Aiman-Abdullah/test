from import_export import resources
from .models import Dim_date, Stage_date


class Stage_date_resource(resources.ModelResource):
    class meta:
        model = Stage_date
        
class Dim_date_resource(resources.ModelResource):
    class meta:
        model = Dim_date