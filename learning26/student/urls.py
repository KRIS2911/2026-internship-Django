from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.studentHome),
    path('sdetail/',views.sdetail),
    path('studentboard/',views.studentboard),
    path('saddress/',views.saddress),
    path('service/',views.servicelist,name="service"),
    path('servicelist/',views.servicelist,name="servicelist"),
    path('createservice/',views.createservice,name="createservice"),
    path('deleteservice/<int:id>/',views.deleteservice,name="deleteservice"),
    
]
