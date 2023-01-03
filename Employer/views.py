from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import * 
from django.db.models import Q

def employe_view(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    all_emp_request=employe_request_form1_permanent.objects.filter(Request_by=Request_by)   
    context={
        'all_emp_request':all_emp_request,
    } 
    return render(request,'employe/index.html',context)

def emp_request(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    Department=(emp.inDepartment)
    request_store=(emp.accessStore)
    checkd_by = employ.objects.get(Q(role = "Dept_Head") & Q(inDepartment=Department))
    if employe_request_form1.objects.filter(Request_by=Request_by).count() !=0:
        employe_request_form1.objects.filter(Request_by=Request_by).delete()
        form1=employe_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
    else:
        form1=employe_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
   
    form1=employe_request_form1.objects.filter(Request_by=Request_by)
    new_form1=form1[0]
    if request.method == "POST":
        employe_request_form2.objects.create(employe_request_form1=new_form1)
    return render(request,'employe/request.html')
def emp_request2(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    form1=employe_request_form1.objects.filter(Request_by=Request_by)
    
    newform=form1[0]
    
    emp_req=employe_request_form2.objects.filter(employe_request_form1=newform)
    context={
        'emp_req':emp_req,
    }
    if form1:
        form1=form1[0]
    if request.method == 'POST':
        Description=request.POST.get("desc")
        unit=request.POST.get("unit")
        req_qty=request.POST.get("qty")
        Remark=request.POST.get("remark")
        form2=employe_request_form2.objects.create(employe_request_form1=form1,Description=Description,unit=unit,req_qty=req_qty,Remark=Remark)
    if form2:
        print("created form 2")
    return render(request,'employe/request.html',context)

def complet_request(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    form1=employe_request_form1.objects.get(Request_by=Request_by)
    Request_by=form1.Request_by
    Department=form1.Department
    request_store=form1.request_store
    checkd_by=form1.checkd_by
    all_items=employe_request_form2.objects.filter(employe_request_form1=form1)
    for item in all_items:
        Description=item.Description
        unit=item.unit
        req_qty=item.req_qty
        Remark=item.Remark
        employe_request_form1_permanent.objects.create( 
            Request_by=Request_by,
            Department=Department,
            request_store=request_store,
            checkd_by=checkd_by,
            Description=Description,
            unit=unit,
            req_qty=req_qty,
            Remark=Remark,)
    return redirect('employe_dashboard')
    

def reste_request_form(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    form1=employe_request_form1.objects.get(Request_by=Request_by)
    employe_request_form2.objects.filter(employe_request_form1=form1).delete()

    return render(request,'employe/request.html',)
def add_employe(request):
    return render(request,'Department_head/add_employe.html',)