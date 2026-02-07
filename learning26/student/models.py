from django.db import models

# Create your models here.

class Student(models.Model):
    studentname=models.CharField(max_length=100)
    studentage=models.IntegerField()
    studentcity=models.CharField(max_length=100)
    studentdiv=models.IntegerField(null=True)
    
    class meta:
        db_table="Student"
        
    def __str__(self):
        return self.studentname
    
        

class Product(models.Model):
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    pcategory=models.CharField(max_length=100)
    pcolor=models.CharField(max_length=100,null=True)
    pstatus=models.BooleanField(default=True)
    
    class meta:
        db_table="Product"
        
### one to one relationship between student and studentdetails     
## one to one relationship means one student can have only one studentdetails and one studentdetails can have only one student. so we have to give one to one field in studentdetails model to connect with student model. and on_delete=models.CASCADE means if we delete the student then the studentdetails related to that student will also be deleted.     
class studentdetails(models.Model):
    hobbies =(("reading","Reading"),("writing","Writing"),("traveling","Traveling"),("music","Music"))
    student_id=models.OneToOneField(Student,on_delete=models.CASCADE)
    studenthobbies=models.CharField(max_length=100,choices=hobbies)
    studentmarks=models.IntegerField()
    studentgrade=models.CharField(max_length=100)
    
    class meta:
        db_table="studentdetails"
        
    def __str__(self):
        return self.student_id.studentname
    
#one to many relationship between category and services 
class Category(models.Model):
    categoryname=models.CharField(max_length=100)
    cdescription=models.CharField(max_length=100)
    cstatus=models.BooleanField(default=True)
    
    class Meta:
        db_table="category"
        verbose_name = "Category"
        verbose_name_plural = "Categories" ## it makes the plural form of category as categories in admin panel
        
    def __str__(self):
        return self.categoryname
  
## catogery is parent and services is child in one to many relationship. so we have to give foreign key in services model to connect with category model. and on_delete=models.CASCADE means if we delete the category then all the services related to that category will also be deleted.  
class services(models.Model):
    servicename=models.CharField(max_length=100)
    servicedescription=models.CharField(max_length=100)
    servicestatus=models.BooleanField(default=True)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    class meta:
        db_table="services"
        
    def __str__(self):
        return self.servicename
    


### Examples of one to one relationship

# one customer has 1 KYC

class Customer(models.Model):
    name=models.CharField(max_length=100)
    bname=models.CharField(max_length=100)
    kycstatus=models.BooleanField(default=False)
    
    class Meta:
        db_table="Customer"

    def __str__(self):
        return self.name

class Kyc(models.Model):
    customer=models.OneToOneField("Customer", verbose_name=("Customers"), on_delete=models.CASCADE)
    id_card=models.IntegerField()
    pan_card=models.IntegerField()
    
    
    class Meta:
        db_table="Kyc"

    def __str__(self):
        return self.customer.name
    
#one to many / many to many relationship

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)

    class Meta:
        db_table="doctor"
    def __str__(self):
        return self.name

class Patient(models.Model):
    doctor=models.ForeignKey("Doctor",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    disease=models.CharField(max_length=100)

    
    class Meta:
        db_table="patient"

    def __str__(self):
        return self.name