from django.contrib import admin
from .models import Student,Product,studentdetails,Category,services,Customer,Kyc,Doctor,Patient


# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(studentdetails)
admin.site.register(Category)
admin.site.register(services)
admin.site.register(Customer)
admin.site.register(Kyc)
admin.site.register(Doctor)
admin.site.register(Patient)
