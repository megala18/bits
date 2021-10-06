from django.contrib import admin
from crudApp.models import Employee
from crudApp.models import Attendance



class EmployeeAdmin(admin.ModelAdmin) :
    list = ['eno', 'ename', 'erole', 'esalary', 'eaddress']

admin.site.register(Employee , EmployeeAdmin)


class AttendanceAdmin(admin.ModelAdmin) :
    list = ['ain', 'aout']

admin.site.register(Attendance , AttendanceAdmin)
