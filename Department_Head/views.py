from django.shortcuts import render
from django.contrib import messages

def dept_head(request):
    
    return render(request,'Department_head/Dashboard/index.html',)

def add_employe(request):
    return render(request,'Department_head/AddNewEmployee/index.html',)

def approve_request(request):
    return render(request,'Department_head/CheckRequest/index.html',)

def make_request(request):
    return render(request,'Department_head/MakeRequest/index.html',)
