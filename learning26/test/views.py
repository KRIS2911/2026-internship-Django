from django.shortcuts import render

# Create your views here.
def parkingHome(request):
    return render(request,"parking/phone.html")
