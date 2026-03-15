from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Course
from .forms import EmployeeForm,CourseForm

# Create your views here.
def employeelist(request):
    # emplist=Employee.objects.all() ## select * from Employee;
    # emplist=Employee.objects.all().values_list() ## in tuple type
    # emplist=Employee.objects.all().values() ## in dictionary type
    emplist=Employee.objects.all().order_by('id').values() ## in asc order
    
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
        return redirect('employeelist')
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
    
# delete Operation
def deleteemployee(request,id):
    ## delete from employees where id=1; 
    print("delete id :",id)
    # deletedemp=Employee.objects.get(id=id)
    Employee.objects.get(id=id).delete()
    # return HttpResponse("First uncomment delete query")
    return redirect('employeelist')
    # return render(request,'employee/employeefilter.html',{'deletedemp':deletedemp})

def filteremployee(request):
    emplist=Employee.objects.filter(age__gte=29)
    return render(request,'employee/employeelist.html',{'emplist':emplist})
    
# it is used to sort the employee list 
# based on age in ascending or 
# descending order based on user input  
# it is based on sort type which is passed as query parameter in url  

def sortedemployee(request, order=None):
    sorttype = order or request.GET.get("sorttype") # allow either path or query parameter
    if sorttype == "asc":
        emplist=Employee.objects.order_by("salary").values()
        return render(request,'employee/employeelist.html',{'emplist':emplist})
    elif sorttype == "desc":
        emplist=Employee.objects.order_by("-salary").values()
        return render(request,'employee/employeelist.html',{'emplist':emplist})
    else:
        return redirect("employeelist")
    


# it is used to sort the employee list in simple way

# def sortedemployee(request,order):
#     if order == "asc":
#         emplist=Employee.objects.order_by("age").values()
#     elif order == "desc":
#         emplist=Employee.objects.order_by("-age").values()
#     else:
#         return HttpResponse("Invalid Sort Type")
    
#     return render(request,'employee/employeelist.html',{'emplist':emplist})
    

## Update Employee 

def updateemployee(request,id):
    # print("Updated ID :",id)
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=employee) # instance is use for get data in form, did not get blank form
        form.save()
        return redirect('employeelist')
    else:
        form=EmployeeForm(instance=employee)
        print("Updated Data.....",request.POST)
        return render(request,'employee/updateemployee.html',{'form':form})
    
