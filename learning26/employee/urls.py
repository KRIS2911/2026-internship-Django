from django.urls import path
from . import views

urlpatterns = [
    path("employeelist/",views.employeelist,name='employeelist'),
    path("employeefilter/",views.employeefilter),
    path("createemployeeform/",views.createEmployeewithForm,name='createemployeeform'),
    path("createcourse/",views.createCourse),
    # path("deleteemployee/",views.deleteemployee,name='deleteemployee')
    path("deleteemployee/<int:id>",views.deleteemployee,name='deleteemployee'),
    path("filteremployee/",views.filteremployee,name='filteremployee'),
    path("sortedemployee/",views.sortedemployee,name='sortedemployee'),
    path("sortedemployee/<str:order>/",views.sortedemployee,name='sortedemployee_by_order'),
    path("updateemployee/<int:id>",views.updateemployee,name='updateemployee')
]
