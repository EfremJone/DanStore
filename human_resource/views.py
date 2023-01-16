from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib import messages
from Store_manager.models import *
from account.models import *
from django.core.mail import send_mail
import random
import string
from random_username.generate import generate_username


def hr_dashboard(request):
    totall_NoEmp=employ.objects.all().count()
    totall_NoDep=department.objects.all().count()
    totall_NoRole=allRole.objects.all().count()
    allEmployees = employ.objects.all()
    allunAprove=unAproved_employees.objects.filter(cheek=None).count()
    context={
        'totall_NoEmp':totall_NoEmp,
        'totall_NoDep':totall_NoDep,
        'totall_NoRole':totall_NoRole,
        'allEmployees':allEmployees,
        'allunAprove':allunAprove,
    }
   
    return render(request,'human_resource/index.html',context)
#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):
    allEmployees = employ.objects.all()
    context = {
        'all_emplyees': allEmployees
    }

    return render(request,'human_resource/ManageEmployee/index.html', context)


def add_new_employe(request):
    all_store=allStore.objects.all()
    context={
        'all_store':all_store,
    }
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        password1 = request.POST.get('temporaryPassword')
        password2 = request.POST.get('temporaryPasswordConfirm')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        role = request.POST.get('role')
        store = request.POST.get('store')
        access_store=allStore.objects.get(pk=store)
        print(access_store)
        Full_Name = firstName +" " + lastName
        if password1 == password2:
            new = User.objects.filter(username=userName)
            if new.count():
                messages.error(request, "User Already Exist")
            else:
                new = User.objects.filter(email=email)
                if new.count():
                    a = new.count()
                   
                    messages.error(request, "Eamil Already Exist")
                else:
                     user = User.objects.create_user(
                         username=userName, email=email, password=password1, first_name=firstName, last_name=lastName)
                     user.save()
                     if user:
                        if role == 'Company_Admin':
                            new_group = Group.objects.get(name='Company_Admin')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender,accessStore=access_store)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif (role == 'Dept_Head'):
                            new_group = Group.objects.get(name='Dept_Head')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender,accessStore=access_store)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif (role == 'Store_Manager'):
                            new_group = Group.objects.get(name='Store_Manager')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender,accessStore=access_store)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif(role == 'Employee'):
                            new_group = Group.objects.get(name='Employe')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender,accessStore=access_store)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif(role == 'Finance'):
                            new_group = Group.objects.get(name='Finance')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender,accessStore=access_store)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        
                        
                   

        else:
            messages.error(request, "password not match")

    return render(request,'human_resource/ManageEmployee/add_new_employee.html',context)
def employe_ditel(request,id):
    req_emp=employ.objects.get(pk=id)
    all_dep=department.objects.all()
    context={
        'req_emp':req_emp,
        'all_dep':all_dep,
    }
    return render(request,'human_resource/ManageEmployee/employe_ditel.html',context)

def aprove_employe(request):
    allUnAprove=unAproved_employees.objects.filter(cheek=None)
    context={
        'allUnAprove':allUnAprove,
    }
    return render(request,'human_resource/ManageEmployee/aprove_employe.html',context)
def unapproveEmploye_ditel(request,id):
    un_employ=unAproved_employees.objects.get(pk=id)
    context={
        'un_employ':un_employ,
    }
    return render(request,'human_resource/ManageEmployee/unapproved_detial.html',context)
def rejected_emp_approved_request(request):
    allUnAprove=unAproved_employees.objects.filter(cheek=False)
    context={
        'allUnAprove':allUnAprove
    }
    return render(request,'human_resource/ManageEmployee/rejected_applicant.html',context)
def reject_request(request,id):
    un_employ=unAproved_employees.objects.get(pk=id)
    un_employ.cheek=False
    un_employ.save()
    return redirect('rejected-emp-approved-request')
def approve_unaproved_emp(request,id):
    

    username= generate_username(1)[0]
    length=8
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    password=result_str
    un_employ=unAproved_employees.objects.get(pk=id)
    un_employ.cheek = True
    un_employ.save()
    print(un_employ.cheek)
    email=un_employ.Emila
    firstName=un_employ.First_Name
    lastName=un_employ.Last_Name
    role=un_employ.role
    gender=un_employ.gender
    access_store1=un_employ.Branch
    access_store=allStore.objects.get(storeName=access_store1)
    Full_Name=firstName + lastName
    address=un_employ.Address
    phone1=un_employ.phone1
    phone2=un_employ.phone2
    profile_pic=un_employ.profile_pic
    Titel=un_employ.Titel
    Filed_Study=un_employ.Filed_Study
    Collage=un_employ.Collage
    grade=un_employ.grade
    Year_Graguation=un_employ.Year_Graguation
    Document=un_employ.Document
    inDepartment=un_employ.Department
    
    new = User.objects.filter(username=username)
    if new.count():
        messages.error(request, "User Already Exist")
    else:
        new = User.objects.filter(email=email)
        if new.count():
                messages.error(request, "Eamil Already Exist")
        else:
            user = User.objects.create_user(
                         username=username, 
                         email=email, 
                         password=password, 
                         first_name=firstName, 
                         last_name=lastName)
            user.save()
           
            if user:
                if  role == 'Employe':
                    new_group = Group.objects.get(name='Employe')
                    new_group.user_set.add(user)
                    newEmployee = employ.objects.create(user=user,
                    role=role,
                    Full_Name=Full_Name,
                    gender=gender,
                    accessStore=access_store,
                    address=address,
                    phone1=phone1,
                    phone2=phone2,
                    Titel=Titel,
                    Filed_Study=Filed_Study,
                    profile_pic=profile_pic,
                    Collage=Collage,
                    grade=grade,
                    Year_Graguation=Year_Graguation,
                    Document=Document,
                    inDepartment=inDepartment
                    )
                    if newEmployee:
                        send_mail(
                                    ' Wellcome DanEnergy ',
                                    'Dear '+ firstName + '\n' + 'This is your username and password \n'+ 'Username: ' +  username + '\n' + 'Password: ' +  password + '\n' + 'Please change your username and password before proceeding.',
                                    'bgiethipia.hade@gmail.com',
                                    [email],
                                    fail_silently=False,)
                        un_employ.cheek = True
                        un_employ.save()
                        messages.success(request,'You Have Successfully Created New Employee')
                        
                        return redirect('hr-manage-employee')
                        
    return redirect('hr-aprove-employe')
    
#----------------- END of manage Employee ---------------#

def hr_department(request):
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
    print(dep_emp)
    context={
        'all_dept': all_depts,
        'data':data
    }
    return render(request,'human_resource/Departments/index.html',context)

def hr_department_detail(request,id):
    DeptHead = employ.objects.filter(role = 'Dept_Head')
    req_dep=department.objects.get(pk=id)
    all_emp=employ.objects.all()
    indep=req_dep.departmentName
    all_employer=employ.objects.filter(inDepartment=indep)
    context={
         "departmentHeads" : DeptHead,
        'selectedDepartment':req_dep,
        'all_emp':all_emp,
        'all_employer':all_employer,
    }
    return render (request,'human_resource/Departments/department_details.html',context)



def add_emp_to_dep(request):
    if request.method == 'POST':
        full_name=request.POST.get('employe')
        dep_name=request.POST.get('departmentName')
        print(full_name)
        print(dep_name)
        selec_dep=department.objects.get(departmentName=dep_name)
        dep=selec_dep.departmentName
        select_emp=employ.objects.get(Full_Name=full_name)
        select_emp.inDepartment=dep
        select_emp.save()
    
    
    return redirect('hr-department-detail',selec_dep.id)
def hr_set_dept_head(request):
    if request.method =="POST":
        dept_id=request.POST.get('departmentId')
        dept_head=request.POST.get('dept_head')
        update_dept=department.objects.get(id=dept_id)
        update_dept.departmentHead = dept_head
        update_dept.save()
        print("dept_id",dept_id)
        print("dept_head",dept_head)
    return redirect('hr-department-detail',dept_id)

def hr_dept_name_change(request):
    if request.method =="POST":
        dept_id=request.POST.get('departmentId')
        dept_name=request.POST.get('deptname')
        update_dept=department.objects.get(id=dept_id)
        update_dept.departmentName = dept_name
        update_dept.save()
        print("dept_id",dept_id)
        print("dept_head",dept_name)
    return redirect('hr-department-detail',dept_id)
def hr_department_delete(request,id):
    department.objects.get(id=id).delete()
    return redirect('hr-department')

def hr_add_new_department(request):
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
            
        return redirect('hr-department')

    return render(request,'human_resource/Departments/add_new_department.html', context)