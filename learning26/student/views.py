from django.shortcuts import render

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