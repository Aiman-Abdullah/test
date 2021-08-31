from django.db import models

# Create your models here.

class dimAudit(models.Model):
    productkey = models.AutoField(primary_key=True)
    productid = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    pdg = models.CharField(max_length=100)
    producttype = models.CharField(max_length=100, null=False)
    dtc = models.CharField(max_length=100, null=False)
    mindeposit = models.CharField(max_length=100, null=True)
    phaseoutdate = models.CharField(max_length=100, null=True)
    discdate = models.CharField(max_length=100,null=True)  #DateTimeField
    discontinued = models.CharField(max_length=100, null=True)
    col = models.CharField(max_length=100, null=False)
    rowiscurrent  = models.CharField(max_length=100, null=False)
    rowstartdate  = models.DateTimeField()
    rowenddate  = models.DateTimeField()
    rowchangereason = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = 'dimaudit'

    def __str__(self):
        return self.productid
