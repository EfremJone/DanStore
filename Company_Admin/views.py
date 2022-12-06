from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Company_Admin/Dashboard/index.html')

def manage_employee(request):
    return render(request,'Company_Admin/ManageEmployee/index.html')

def page2(request):
    return render(request,'Company_Admin/page2.html')

def page3(request):
    return render(request,'Company_Admin/page3.html')

def page4(request):
    return render(request,'Company_Admin/page4.html')

def page5(request):
    return render(request,'Company_Admin/page5.html')

def page6(request):
    return render(request,'Company_Admin/page6.html')

def page7(request):
    return render(request,'Company_Admin/page7.html')