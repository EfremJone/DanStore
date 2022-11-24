from django.shortcuts import render

# Create your views here.

def store_dashboard(request):
    return render(request,'Store_manager/dashboard.html')

def manage_catagory(request):
    return render(request,'Store_manager/Catagory/manage_catagory.html')
def add_to_store(request):
    return render(request,"Store_manager/Add_to_Store/add_to_store.html")

def cheeck_request(request):
    return render(request,"Store_manager/cheeck_Request/cheeck_request.html")