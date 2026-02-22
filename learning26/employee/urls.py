from django.urls import path
from . import views

urlpatterns = [
    path("employeelist/",views.employeelist),
    path("employeefilter/",views.employeefilter),
    path("createemployeeform/",views.createEmployeewithForm),
    path("createcourse/",views.createCourse),
    
]