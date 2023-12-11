from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Employee
# Create your views here.


def index(request):
    #return HttpResponse(f"<h1>{request.tenant} Index </h1>")
    employees = Employee.objects.all()
    return render(request, "client_index.html", {"employees": employees})
def CreateEmployee(request):
    # employee = Employee(name=name)
    # employee.save()
    # return HttpResponse(f"<h1> {request.tenant} employee created</h1>")
    if request.POST:
        name = request.POST.get("name")
        employee = Employee(name=name)
        employee.save()
        return redirect("client_index") # path of index (view)