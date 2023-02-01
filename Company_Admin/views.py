from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group
from Department_Head.models import *
from django.contrib import messages
from django.shortcuts import render,redirect
from itertools import chain
# Create your views here.

def home(request):
    allDep=department.objects.all()
    deptLength = allDep.__len__()
    allstores=allStore.objects.all()
    allDep=department.objects.all()
    allemp=employ.objects.all()
    emplength=allemp.__len__()
    context={
        'deptLength': deptLength,
        'allstores':allstores,
        'allDep':allDep,
        'emplength':emplength,
        'allemp':allemp,
    }
    return render(request,'Company_Admin/Dashboard/index.html',context)

def user_profile(request):
    return render(request,'Company_Admin/EditProfile/show_profile.html')
def deparetment_dashboard(request):
    allDep=department.objects.all()
    deptLength = allDep.__len__()
    allstores=allStore.objects.all()
    allDep=department.objects.all()
    allemp=employ.objects.all()
    emplength=allemp.__len__()
    context={
        'deptLength': deptLength,
        'allstores':allstores,
        'allDep':allDep,
        'emplength':emplength,
        'allemp':allemp,
    }
    
    return render(request,'Company_Admin/Dashboard/departments.html',context)

def employees_dashboard(request):
    allDep=department.objects.all()
    deptLength = allDep.__len__()
    allstores=allStore.objects.all()
    allDep=department.objects.all()
    allemp=employ.objects.all()
    emplength=allemp.__len__()
    context={
        'deptLength': deptLength,
        'allstores':allstores,
        'allDep':allDep,
        'emplength':emplength,
        'allemp':allemp,
    }
    return render(request,'Company_Admin/Dashboard/employees.html',context)
#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):

    allEmployees = employ.objects.all()
    context = {
        'all_emplyees': allEmployees
    }

    return render(request,'Company_Admin/ManageEmployee/index.html', context)


def item_in_employee(request,id):
    item_rec_emp=employ.objects.get(id=id)
    Request_by=item_rec_emp.Full_Name
    all_emp_request_in_me=employe_request_form1_permanent.objects.filter(Q(Request_by=Request_by) & Q(Store_Keeper_Action='Allowed') & Q(dept_head_Action="Approved") & Q(Recival_status_by_Employer='Received'))  
    
    context={
       'all_emp_request_in_me':all_emp_request_in_me,
       'Request_by':Request_by,
    }
    return render(request,'Company_Admin/ManageEmployee/item_in_employee.html',context)

#----------------- END of manage Employee ---------------#


#----------------- DEPARTMENTS ---------------#

def departments(request):
    all_depts = department.objects.all()
    dep_emp={}
    all_dep_name=[]
    num=[]
    for dep in all_depts:
            all_dep_name.append(dep.departmentName)
    
    for dep in all_dep_name:
        dep_emp[dep]=employ.objects.filter(inDepartment=dep).count()
    for i,j in dep_emp.items():
        num.append(j)
    data=zip(all_depts, num)
    context={
        'all_dept': all_depts,
        'data':data,
    }
    
    return render(request,'Company_Admin/Departments/index.html', context)

def add_new_department(request):
    DeptHead = employ.objects.filter(role = 'Dept_Head')
    
    context = {
        "departmentHeads" : DeptHead
    }
    if request.method == 'POST':
        departmentName = request.POST.get('departmentName')
        departmentDescription = request.POST.get('departmentDescription')
        
        dept = department.objects.create(departmentName = departmentName,departmentDescription=departmentDescription)
        if dept:
            messages.success(request,'You Have Successfully added new department.')
            
        return redirect('departments')

    return render(request,'Company_Admin/Departments/add_new_department.html', context)

def item_in_each_department(request,id):
    req_dep=department.objects.get(pk=id)
    dep_head=req_dep.departmentHead
    re_employ=employ.objects.get(Full_Name=dep_head)
    print(re_employ)
    checkd_by=re_employ
    Request_by=re_employ.Full_Name
    requ_by_dept_recv=dept_request_form1_permanent.objects.filter (Q(Request_by=Request_by) & Q(Store_Keeper_Action="Allowed") | Q(Recival_status_by_Employer='Received')).order_by("-id") 
    requ_by_emp_recv=employe_request_form1_permanent.objects.filter(Q(checkd_by=checkd_by) & Q(Store_Keeper_Action="Allowed") | Q(Recival_status_by_Employer='Received')).order_by("-id") 
    all_receved_req=list(chain(requ_by_dept_recv, requ_by_emp_recv))
    context={
        
        'all_receved_req':all_receved_req,
    }
    
    return render(request,'Company_Admin/Departments/department_details.html', context)
def set_dept_head(request):
    if request.method =="POST":
        dept_id=request.POST.get('departmentId')
        dept_head=request.POST.get('dept_head')
        update_dept=department.objects.get(id=dept_id)
        update_dept.departmentHead = dept_head
        update_dept.save()
        print("dept_id",dept_id)
        print("dept_head",dept_head)
    return redirect('department-details',dept_id)

def department_delete(request,id):
    tobedeleted = department.objects.filter(pk=id).delete()
    if tobedeleted:
        
        messages.success(request,'You Have Successfully deleted the department')
        return redirect('departments')

#----------------- END of Departments ---------------#


#----------------- VENDORS ---------------#
def vendors(request):
    allVendors = vendor.objects.all()
    context = {
        'allVendors': allVendors
    }
    return render(request,'Company_Admin/Vendors/index.html',context)

def vendor_detail(request,id):
    selectedVendor = vendor.objects.get(pk=id)
    context = {
        'selectedVendor': selectedVendor
    }
    return render(request,'Admin/Vendors/vendor_details.html',context)

def add_new_vendor(request):

    if request.method == 'POST':
        # vendorCode = request.POST.get('vendorCode')
        vendorName = request.POST.get('vendorName')
        vendorProducts = request.POST.get('vendorProducts')
        vendorOrigin = request.POST.get('vendorOrigin')
        vendorType = request.POST.get('vendorType')

        ven = vendor.objects.create(vendorName=vendorName,vendorProducts=vendorProducts,vendorOrigin=vendorOrigin,vendorType=vendorType)
        if ven:
            messages.success(request,'You Have Successfully added new vendor.')
            
        return redirect('vendors')

    return render(request, 'Company_Admin/Vendors/add_new_vendor.html')

#----------------- END of VENDORS ---------------#

#----------------- ROLE ---------------#

def role(request):
    
    allRoles = allRole.objects.all()
    context={
        'allRoles': allRoles
    }
    return render(request,'Company_Admin/Role/role_details.html',context)

#----------------- END of ROLE ---------------#


#----------------- STORE ---------------#
def store(request):
    stores = allStore.objects.all()
    context ={
        'stores': stores
    }
    return render(request,'Company_Admin/Store/index.html', context)

def store_details(request,id):
    store=allStore.objects.get(pk=id)
    all_category = Catagory.objects.filter(store=id)
    all_category.storeId = id
    storeKeepers = employ.objects.filter(role = 'Store_Manager')
    context = {
        'all_category': all_category,
        'storeId':id,
        'store':store,
        'storeKeepers': storeKeepers
    }
    if request.method == "POST":
        new_store_name=request.POST.get('store_name')
        store.storeName =new_store_name
        store.save()
        print(new_store_name)
    return render(request,"Company_Admin/Store/store_detail.html", context)

def delete_store(request,id):
    allStore.objects.get(pk=id).delete()
    return redirect('store')
def add_new_store(request):
    storeKeepers = employ.objects.filter(role = 'Store_Manager')
    context={
        'storeKeepers': storeKeepers
    }

    if request.method == 'POST':
        storeName = request.POST.get('storeName')
        storeDescription = request.POST.get('storeDescription')
        
        storeLocation = request.POST.get('storeLocation')


        addedStore = allStore.objects.create(storeName=storeName,storeDescription=storeDescription,storeLocation=storeLocation)
        if addedStore:
            return redirect('store')
        
    return render(request, 'Company_Admin/Store/add_new_store.html', context)
def store_manager_update(request,id):
    store=allStore.objects.get(id=id)
    if request.method == "POST":
        new_store_keeper=request.POST.get("store_keeper")
        store.storeKeeper=new_store_keeper
        store.save()
        print("This is store manager",new_store_keeper)
    return redirect('store-details',id)
def cat_item_detail(request,id):
    category = Catagory.objects.get(pk=id)
    context={
        'category':category
    }
    return render(request, 'Company_Admin/Store/cat_item_details.html',context)

#----------------- End OF STORE ---------------#

def reports(request):
    return render(request,'Company_Admin/Reports/index.html')

def chat(request):
    chat_group=employ.objects.all()
    if request.method == 'POST':
        user=request.POST.get('serach')
        serch=User.objects.get(username=user)
        chat_group1=employ.objects.get(user=serch)
   
        context={
            
            'chat_group1':chat_group1,
        }
        return render(request,'Company_Admin/chat/index1.html',context)
    context={
      
        'chat_group':chat_group,
    }
    return render(request,'Company_Admin/chat/index.html',context)

def chat_pepol(request,id):
    chat_employ=employ.objects.get(pk=id)
    me=employ.objects.get(pk=request.user.id)
    all_message=chatbot.objects.filter(Q(Q(me_with=chat_employ) | Q(me=chat_employ)) & Q(Q(me_with=me) | Q(me=me)))
    if request.method == 'POST':
        me_with=employ.objects.get(pk=id)
        me=me
        message=request.POST.get('mess')
        newmess=chatbot.objects.create(me_with=me_with,me=me,message=message)
        if newmess:
            return redirect('admin-chat_people',id)
    context={
        'chat_employ':chat_employ,
        'message':all_message,
        'id':id,
        'me':me
    }
    return render(request,'Company_Admin/chat/chat.html',context)
def chat_profile(request,id):
    chat_employ=employ.objects.get(pk=id)
    context={
        'chat_employ':chat_employ,
    }
    return render(request,'Company_Admin/chat/profile.html',context)
def send_message(request):
    me=request.user
    if request.method == 'POST':
       pass
    return redirect('admin-chat_people')



def Purchase_item(request):
    all_perch_item=form2permanent.objects.all()
    context={
        'all_perch_item':all_perch_item
    }
    return render(request,'Company_Admin/Purchase_item/Approve_purchase_item.html')