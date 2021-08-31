from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)   
    personemail = models.EmailField()
    location = models.CharField(max_length=50,blank=True)

    class Meta:
        managed = False
        db_table = 'teststageperson'
