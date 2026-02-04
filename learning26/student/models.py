from django.db import models

# Create your models here.

class Student(models.Model):
    studentname=models.CharField(max_length=100)
    studentage=models.IntegerField()
    studentcity=models.CharField(max_length=100)
    studentdiv=models.IntegerField(null=True)
    
    class meta:
        db_table="Student"
        

class Product(models.Model):
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    pcategory=models.CharField(max_length=100)
    pcolor=models.CharField(max_length=100,null=True)
    pstatus=models.BooleanField(default=True)
    
    class meta:
        db_table="Product"