from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Course
from .forms import EmployeeForm,CourseForm

# Create your views here.
def employeelist(request):
    # emplist=Employee.objects.all() ## select * from Employee;
    # emplist=Employee.objects.all().values_list() ## in tuple type
    emplist=Employee.objects.all().values() ## in dictionary type
    
    # print(emplist)
    return render(request,'employee/employeelist.html',{'emplist':emplist})

def employeefilter(request):
    empname=Employee.objects.filter(name="kris").values()
    empid=Employee.objects.filter(id = 2).values()
    emppost=Employee.objects.filter(post = "developer").values()
    empidandpost=Employee.objects.filter(name="kris",post="engineer").values()
    empgt=Employee.objects.filter(age__gt=21).values()
    empgte=Employee.objects.filter(age__gte=21).values()
    
    ## string Queries 
    empexact=Employee.objects.filter(post__exact="engineer").values()
    empiexact=Employee.objects.filter(post__iexact="Engineer").values()
    empcontains=Employee.objects.filter(name__contains="i").values()
    empicontains=Employee.objects.filter(name__icontains="I").values()
    
    empstartswith=Employee.objects.filter(name__startswith="m").values()
    empistartswith=Employee.objects.filter(name__istartswith="M").values()
    empendswith=Employee.objects.filter(name__endswith="j").values()
    empiendswith=Employee.objects.filter(name__iendswith="J").values()
    
    empin=Employee.objects.filter(name__in=["kris","raj"]).values()
    emprange=Employee.objects.filter(age__range=(22,25)).values()
    
    emporderA=Employee.objects.order_by("age").values() # asc
    emporderD=Employee.objects.order_by("-age").values() # desc
    
    employeef={
        "empname":empname,
        "empid":empid,
        "emppost":emppost,
        "empidandpost":empidandpost,
        "empgt":empgt,
        "empgte":empgte,
        "empexact":empexact,
        "empiexact":empiexact,
        "empcontains":empcontains,
        "empicontains":empicontains,
        "empstartswith":empstartswith,
        "empistartswith":empistartswith,
        "empendswith":empendswith,
        "empiendswith":empiendswith,
        "empin":empin,
        "emprange":emprange,
        "emporderA":emporderA,
        "emporderD":emporderD,
        
    } 
    return render(request,'employee/employeefilter.html',{'employeef':employeef})

## create Employee form
def createEmployeewithForm(request):
    if request.method == "POST":
        form=EmployeeForm(request.POST)
        form.save()
        return HttpResponse("Successfully Created Employee")
    else:
        form=EmployeeForm()
        return render(request,"employee/createemployeeform.html",{"form":form})
    
## create course form 

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save()
        return HttpResponse("Course Successfully Created......")
    
    else:
        form = CourseForm()
        return render(request,"employee/createcourseform.html",{"form":form})