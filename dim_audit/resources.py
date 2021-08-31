from import_export import resources
from .models import dimAudit 

class dimAuditResource(resources.ModelResource):
    class meta:
        model = dimAudit