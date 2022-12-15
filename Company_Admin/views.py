from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group

# Create your views here.

def home(request):
    cate = Catagory.objects.all()
    vend = vendor.objects.all()
    dept = department.objects.all()
    cateLength = cate.__len__()
    vendLenth = vend.__len__()
    deptLength = dept.__len__()
    context={
        'cateLength': cateLength,
        'vendLength': vendLenth,
        'deptLength': deptLength
    }
    return render(request,'Admin/Dashboard/index.html',context)

def user_profile(request):
    return render(request,'Admin/EditProfile/show_profile.html')

#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):

    allEmployees = employ.objects.all()
    context = {
        'all_emplyees': allEmployees
    }

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        temporaryPassword = request.POST.get('temporaryPassword')
        temporaryPasswordConfirm = request.POST.get('temporaryPasswordConfirm')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        role = request.POST.get('role')
        Full_Name = firstName +" " + lastName
        # print("data: first name:",firstName," last name: ",lastName," user name: ", userName, " temp pass: ", temporaryPassword, " temporary pass con: ", temporaryPasswordConfirm," gender: ",gender, " email: ", email," role: ",role )
        user= User.objects.create(first_name=firstName,last_name=lastName,username= userName,password=temporaryPassword,email=email,)
        if user:
            if role == 'Company_Admin':
                new_group = Group.objects.get(name='Company_Admin')
                new_group.user_set.add(user)
                newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                if newEmployee:
                    print("new emplyee created.")
            elif (role == 'Dept_Head'):
                new_group = Group.objects.get(name='Dept_Head')
                new_group.user_set.add(user)
                newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                if newEmployee:
                    print("new emplyee created.")
            elif (role == 'Store_Manager'):
                new_group = Group.objects.get(name='Store_Manager')
                new_group.user_set.add(user)
                newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                if newEmployee:
                    print("new emplyee created.")
            elif(role == 'Employee'):
                new_group = Group.objects.get(name='Employee')
                new_group.user_set.add(user)
                newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                if newEmployee:
                    print("new employee created.")
            elif(role == 'Finance'):
                new_group = Group.objects.get(name='Finance')
                new_group.user_set.add(user)
                newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                if newEmployee:
                    print("new employee created.")
            print('successfully added new user')
        else:
            print("some error happend")
        return redirect('manage-employee')
    return render(request,'Admin/ManageEmployee/index.html', context)

def add_new_employee(request):
    return render(request,'Admin/ManageEmployee/add_new_employee.html')

#----------------- END of manage Employee ---------------#


#----------------- DEPARTMENTS ---------------#

def departments(request):

    if request.method == 'POST':
        deptId = request.POST.get('deptId')

        print("this is going to be deleted.", deptId)

    all_depts = department.objects.all()
    context={
        'all_dept': all_depts
    }
    
    return render(request,'Admin/Departments/index.html', context)

def add_new_department(request):
    DeptHead = employ.objects.filter(role = 'Dept_Head')
    
    context = {
        "departmentHeads" : DeptHead
    }
    if request.method == 'POST':
        departmentName = request.POST.get('departmentName')
        departmentDescription = request.POST.get('departmentDescription')
        departmentHead = request.POST.get('departmentHead')

        dept = department.objects.create(departmentName = departmentName,departmentDescription=departmentDescription,departmentHead=departmentHead)
        if dept:
            print("successfully added new department")
        return redirect('departments')

    return render(request,'Admin/Departments/add_new_department.html', context)

def department_details(request,id):
    if request.method == 'POST':
        updatedDepartmentName = request.POST.get('updatedDepartmentName')
        departmentId = request.POST.get('departmentId')
        toBeUpdate = department.objects.filter(id=departmentId).update(departmentName=updatedDepartmentName)
        if toBeUpdate:
            print("successfully updated the department Name")
    selectedDepartment = department.objects.get(pk=id)
    memebers = employ.objects.filter(inDepartment = selectedDepartment.id)
    context={
        'selectedDepartment': selectedDepartment,
        'members': memebers
    }
    return render(request,'Admin/Departments/department_details.html', context)

def department_delete(request,id):
    tobedeleted = department.objects.filter(pk=id).delete()
    if tobedeleted:
        print("successfully deleted the department")
        return redirect('departments')

#----------------- END of Departments ---------------#


#----------------- VENDORS ---------------#
def vendors(request):
    allVendors = vendor.objects.all()
    context = {
        'allVendors': allVendors
    }
    return render(request,'Admin/Vendors/index.html',context)

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
            print('successfully added new vendor.')
        return redirect('vendors')

    return render(request, 'Admin/Vendors/add_new_vendor.html')

#----------------- END of VENDORS ---------------#

#----------------- ROLE ---------------#

def role(request):
    
    allRoles = allRole.objects.all()
    context={
        'allRoles': allRoles
    }
    return render(request,'Admin/Role/index.html',context)

def add_new_role(request):
    return render(request, 'Admin/Role/add_new_role.html')

def role_details(request,id):
    selectedRole = allRole.objects.get(pk=id)
    context={
        'selectedRole': selectedRole
    }
    return render(request, 'Admin/Role/role_details.html',context)

#----------------- END of ROLE ---------------#


#----------------- STORE ---------------#
def store(request):
    stores = allStore.objects.all()
    context ={
        'stores': stores
    }
    return render(request,'Admin/Store/index.html', context)

def store_details(request,id):
    all_category = Catagory.objects.filter(store=id)
    all_category.storeId = id
    print('category are: ',all_category.storeId)
    context = {
        'all_category': all_category,
        'storeId':id
    }
    print(all_category)
    return render(request,"Admin/Store/store_detail.html", context)

def add_new_store(request):
    storeKeepers = employ.objects.filter(role = 'Store_Manager')
    context={
        'storeKeepers': storeKeepers
    }

    if request.method == 'POST':
        storeName = request.POST.get('storeName')
        storeDescription = request.POST.get('storeDescription')
        storeKeeper = request.POST.get('storeKeeper')
        storeLocation = request.POST.get('storeLocation')


        addedStore = allStore.objects.create(storeName=storeName,storeDescription=storeDescription,storeKeeper=storeKeeper,storeLocation=storeLocation)
        if addedStore:
            return redirect('store')
        
    return render(request, 'Admin/Store/add_new_store.html', context)

def cat_item_detail(request,id):
    category = Catagory.objects.get(pk=id)
    context={
        'category':category
    }
    return render(request, 'Admin/Store/cat_item_details.html',context)

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