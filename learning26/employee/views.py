from django.shortcuts import render
from .models import Employee

# Create your views here.
def employeelist(request):
    # emplist=Employee.objects.all() ## select * from Employee;
    # emplist=Employee.objects.all().values_list() ## in tuple type
    emplist=Employee.objects.all().values() ## in dictionary type
    
    print(emplist)
    return render(request,'employee/employeelist.html',{'emplist':emplist})