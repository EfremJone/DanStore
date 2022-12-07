from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Admin/Dashboard/index.html')

#----------------- manage Employee ---------------#
def manage_employee(request):
    return render(request,'Admin/ManageEmployee/index.html')

def add_new_employee(request):
    return render(request,'Admin/ManageEmployee/add_new_employee.html')

#----------------- END of manage Employee ---------------#

def departments(request):
    return render(request,'Admin/Departments/index.html')

def vendors(request):
    return render(request,'Admin/Vendors/index.html')

def role(request):
    return render(request,'Admin/Role/index.html')

# def categories(request):
#     return render(request,'Admin/Categories/index.html')
#----------------- store ---------------#
def store(request):
    return render(request,'Admin/Store/index.html')

def store_details(request):
    return render(request,"Admin/Store/store_detail.html")
#----------------- End store ---------------#
def batch(request):
    return render(request,'Admin/Batch/index.html')

def reports(request):
    return render(request,'Admin/Reports/index.html')

def chat(request):
    return render(request,'Admin/Chat/index.html')

def chat_people(request):
    return render(request,'Admin/Chat/chat.html')