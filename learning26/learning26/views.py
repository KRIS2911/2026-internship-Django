from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def test(request):
    return HttpResponse("HEllo")
def contactus(request):
    return render(request,"contactus.html")
def aboutus(request):
    return render(request,"aboutus.html")

## For Movie,show & news

def movie(request):
    return render(request,"movie.html")
def show(request):
    return render(request,"show.html")
def news(request):
    return render(request,"news.html")