from django.shortcuts import render
from django.contrib import messages
from Store_manager.models import *


def dept_head(request):
    curretnUser = request.user
    exploreU = employ.objects.filter(user = curretnUser)
    print("shit",exploreU.inDepartment)
    context = {
        'userData' : exploreU
    }
    
    return render(request,'Department_head/Dashboard/index.html', context)

def add_employe(request):
    allEmps = employ.objects.filter(role = "Employee")
    context = {
        'allEmps' : allEmps
    }
    return render(request,'Department_head/AddNewEmployee/index.html',context)

def approve_request(request):
    return render(request,'Department_head/CheckRequest/index.html',)

def make_request(request):
    return render(request,'Department_head/MakeRequest/index.html',)
