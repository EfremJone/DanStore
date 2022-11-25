from django.shortcuts import render

# Create your views here.

def store_dashboard(request):
    return render(request,'Company_Admin/admin_base.html')