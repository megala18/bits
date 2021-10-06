from django import forms
from crudApp.models import Employee
from crudApp.models import Attendance

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
     class Meta:
         model = Attendance
         fields = '__all__' 
