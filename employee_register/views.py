from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

from django.contrib.auth.decorators import login_required

# Create your views here.

# USE request.user.get_username() to get username in views

# from django.http import HttpResponseRedirect
# def dimProduct(request):
#     return HttpResponseRedirect("/dim_product")

@login_required(login_url="/accounts/login/")
def dim_color(request):
    return redirect(request,'/dim_color')

@login_required(login_url="/accounts/login/")
def dim_customer(request):
    return redirect(request,'/dim_customer')

@login_required(login_url="/accounts/login/")
def dim_date(request):
    return redirect(request,'/dim_date')

@login_required(login_url="/accounts/login/")
def dim_discount(request):
    return redirect(request,'/dim_discount')

@login_required(login_url="/accounts/login/")
def dim_product(request):
    return redirect(request,'/dim_product')

@login_required(login_url="/accounts/login/")
def dim_product_group(request):
    return redirect(request,'/dim_product_group')

@login_required(login_url="/accounts/login/")
def fact_sales_order_item(request):
    return redirect(request,'/fact_sales_order_item')

@login_required(login_url="/accounts/login/")
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "employee_register/employee_list.html",context)

@login_required(login_url="/accounts/login/")
def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm() 
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form':form})
    else:
        if id == 0:
            form = EmployeeForm (request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

@login_required(login_url="/accounts/login/")
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')


'''

def simple_upload(request):
if request.method == 'POST':
    person_resource = PersonResource()
    dataset = Dataset()
    new_persons = request.FILES['myfile']

    imported_data = dataset.load(new_persons.read(),format='xlsx')
    #print(imported_data)
    for data in imported_data:
        print(data[1])
        value = Person(
            data[0],
            data[1],
                data[2],
                data[3]
            )
        value.save()       
    
    #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

    #if not result.has_errors():
    #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

return render(request, 'input.html')
'''