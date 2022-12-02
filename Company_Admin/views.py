from django.shortcuts import render

# Create your views here.

def admin_dashboard(request):
    return render(request,'Company_Admin/index.html')
def add_user(request):
    name="Efrem"
    context={
        'name':name
    }
    return render(request,'Company_Admin/new.html',context)