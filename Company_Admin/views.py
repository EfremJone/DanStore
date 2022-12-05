from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Admin/index.html')
def page1(request):
    return render(request,'Admin/page1.html')
def page2(request):
    return render(request,'Admin/page2.html')
def page3(request):
    return render(request,'Admin/page3.html')
def page4(request):
    return render(request,'Admin/page4.html')
def page5(request):
    return render(request,'Admin/page5.html')
def page6(request):
    return render(request,'Admin/page6.html')
def page7(request):
    return render(request,'Admin/page7.html')