from django.shortcuts import render
from django.contrib import messages
def dept_head(request):
    
    return render(request,'Department_head/index.html',)

def add_employe(request):

    return render(request,'Department_head/add_employe.html',)

def approve_request(request):
    
    return render(request,'Department_head/check_request.html',)

def make_request(request):
    return render(request,'Department_head/make_request.html',)
