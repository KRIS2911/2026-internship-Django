from django import forms
from .models import Employee,Course

class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields="__all__"

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = ["name","fees"] 
        fields="__all__"# [name,fees,duration]
