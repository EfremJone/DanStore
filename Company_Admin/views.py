from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,'Admin/Dashboard/index.html')

#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):
    return render(request,'Admin/ManageEmployee/index.html')

def add_new_employee(request):
    return render(request,'Admin/ManageEmployee/add_new_employee.html')

#----------------- END of manage Employee ---------------#


#----------------- DEPARTMENTS ---------------#

def departments(request):
    return render(request,'Admin/Departments/index.html')

def add_new_department(request):
    return render(request,'Admin/Departments/add_new_department.html')

def department_details(request):
    return render(request,'Admin/Departments/department_details.html')

#----------------- END of Departments ---------------#


#----------------- VENDORS ---------------#
def vendors(request):
    return render(request,'Admin/Vendors/index.html')

def add_new_vendor(request):
    return render(request, 'Admin/Vendors/add_new_vendor.html')

#----------------- END of VENDORS ---------------#

#----------------- ROLE ---------------#

def role(request):
    return render(request,'Admin/Role/index.html')

def add_new_role(request):
    return render(request, 'Admin/Role/add_new_role.html')

def role_details(request):
    return render(request, 'Admin/Role/role_details.html')

#----------------- END of ROLE ---------------#


#----------------- STORE ---------------#
def store(request):
    return render(request,'Admin/Store/index.html')

def store_details(request):
    return render(request,"Admin/Store/store_detail.html")

def add_new_store(request):
    return render(request, 'Admin/Store/add_new_store.html')

def cat_item_detail(request):
    return render(request, 'Admin/Store/cat_item_details.html')

#----------------- End OF STORE ---------------#

def reports(request):
    return render(request,'Admin/Reports/index.html')

def chat(request):
    chat_group=employ.objects.all()
    if request.method == 'POST':
        user=request.POST.get('serach')
        serch=User.objects.get(username=user)
        chat_group1=employ.objects.get(user=serch)
   
        context={
            
            'chat_group1':chat_group1,
        }
        return render(request,'Admin/chat/index1.html',context)
    context={
      
        'chat_group':chat_group,
    }
    return render(request,'Admin/chat/index.html',context)

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
    return render(request,'Admin/chat/chat.html',context)
def chat_profile(request,id):
    chat_employ=employ.objects.get(pk=id)
    context={
        'chat_employ':chat_employ,
    }
    return render(request,'Admin/chat/profile.html',context)
def send_message(request):
    me=request.user
    if request.method == 'POST':
        print(me)
    return redirect('admin-chat_people')