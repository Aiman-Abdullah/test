from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

# Use the three commands below to migrate models into database

'''
python manage.py makemigrations employee_register

python manage.py sqlmigrate employee_register 0001

python manage.py migrate

'''