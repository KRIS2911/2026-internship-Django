from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.studentHome),
    path('sdetail/',views.sdetail),
    path('studentboard/',views.studentboard),
    path('saddress/',views.saddress),
]