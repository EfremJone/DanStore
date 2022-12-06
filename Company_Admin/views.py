from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Admin/Dashboard/index.html')

def manage_employee(request):
    return render(request,'Admin/ManageEmployee/index.html')

def departments(request):
    return render(request,'Admin/Departments/index.html')

def vendors(request):
    return render(request,'Admin/Vendors/index.html')

def role(request):
    return render(request,'Admin/Role/index.html')

def products(request):
    return render(request,'Admin/Products/index.html')

def store(request):
    return render(request,'Admin/Store/index.html')

def batch(request):
    return render(request,'Admin/Batch/index.html')

def reports(request):
    return render(request,'Admin/Reports/index.html')

def chat(request):
    return render(request,'Admin/Chat/index.html')

def chat_people(request):
    return render(request,'Admin/Chat/chat.html')