from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Admin/Dashboard/index.html')

#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):
    return render(request,'Admin/ManageEmployee/index.html')

def add_new_employee(request):
    return render(request,'Admin/ManageEmployee/add_new_employee.html')

#----------------- END of manage Employee ---------------#


#----------------- DEPARTMENTS ---------------#

def departments(request):
    return render(request,'Admin/Departments/index.html')

def add_new_department(request):
    return render(request,'Admin/Departments/add_new_department.html')
#----------------- END of Departments ---------------#


#----------------- VENDORS ---------------#
def vendors(request):
    return render(request,'Admin/Vendors/index.html')

def add_new_vendor(request):
    return render(request, 'Admin/Vendors/add_new_vendor.html')

#----------------- END of VENDORS ---------------#

#----------------- ROLE ---------------#

def role(request):
    return render(request,'Admin/Role/index.html')
#----------------- END of ROLE ---------------#

# def categories(request):
#     return render(request,'Admin/Categories/index.html')

#----------------- STORE ---------------#
def store(request):
    return render(request,'Admin/Store/index.html')

def store_details(request):
    return render(request,"Admin/Store/store_detail.html")

def add_new_store(request):
    return render(request, 'Admin/Store/add_new_store.html')

def cat_item_detail(request):
    return render(request, 'Admin/Store/cat_item_details.html')

#----------------- End OF STORE ---------------#
def batch(request):
    return render(request,'Admin/Batch/index.html')

def reports(request):
    return render(request,'Admin/Reports/index.html')

def chat(request):
    return render(request,'Admin/Chat/index.html')

def chat_people(request):
    return render(request,'Admin/Chat/chat.html')