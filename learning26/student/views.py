from django.shortcuts import render, redirect,get_object_or_404
from .models import services
from .forms import ServiceForm
from django.contrib import messages

# Create your views here.

def studentHome(request):
    data={
        "schoolname":"Royal",
        "domain":"Django"
    }
    return render(request,"student/studentHome.html",data)

def sdetail(request):
    name=["kris","diya","ram","ravan"]
    sdata={
        "name":name,
        "std":5,
        "r_no":6
    }
    return render(request,"student/sdetail.html",sdata)

def studentboard(request):
    marks={
        "maths":90,
        "science":85,
        "english":88
    }
    return render(request,"student/studeboard.html",marks)

def saddress(request):
    address={
        "city":"Chennai",
        "state":"Tamilnadu",
        "country":"India"
    }
    return render(request,"student/saddress.html",address)

def servicelist(request):
    service_list = services.objects.all()
    return render(request,"student/service.html",{"services":service_list})

def createservice(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
        else:
            return render(request, "student/createservice.html", {"form": form})
    else:
        form = ServiceForm()
        return render(request, "student/createservice.html", {"form": form})

# def deleteservice(request, id):
#     service = services.objects.get(id=id)
#     service.delete()
#     return redirect("servicelist")

    
def deleteservice(request, id):
    service = get_object_or_404(services, id=id)

    if request.method == "POST":
        service.delete()
        messages.success(request, "Service deleted successfully.")
        return redirect("servicelist")

    return render(request, "student/confirm_delete.html", {"service": service})


    
        
