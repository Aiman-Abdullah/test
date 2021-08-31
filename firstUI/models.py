from django.db import models

# Create your models here.

class Tempcolor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    colordescription = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempcolor'

'''
    def __str__(self):
        return self.name

'''

