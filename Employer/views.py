from django.shortcuts import render
from django.contrib import messages
def employe_view(request):
    
    return render(request,'employe/index.html',)

def request(request):
    return render(request,'employe/request.html',)

def add_employe(request):
    return render(request,'Department_head/add_employe.html',)