from django.shortcuts import render,redirect
from crudApp.models import Employee
from crudApp.models import Attendance
from crudApp.forms import EmployeeForm
from crudApp.forms import AttendanceForm

def retrieve_view(request):
    employee = Employee.objects.all()
    return render(request,'crudApp/index.html',{'employee':employee})

def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudApp/create.html',{'form': form})

def delete_view(request,id):
     employee = Employee.objects.get(id=id)
     employee.delete()
     return redirect('/check')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST ,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudApp/update.html',{'employee': employee})



def retrieve_view(request):
    attendance = Attendance.objects.all()
    return render(request,'crudApp/index.html',{'attendance':attendance})

def create_view(request):
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudApp/create.html',{'form': form})

def delete_view(request,id):
     attendance = Attendance.objects.get(id=id)
     attendance.delete()
     return redirect('/check')

def update_view(request,id):
    attendance = Attendance.objects.get(id=id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST ,instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudApp/update.html',{'attendance': attendance})