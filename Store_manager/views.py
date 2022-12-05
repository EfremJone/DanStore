from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from .form import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect


def store_dashboard(request):
    all_catagory = Catagory.objects.all()
    context ={
        'all_catagory':all_catagory,
    }
    return render(request,'Store_manager/dashboard.html',context)

def manage_catagory(request):
    
    all_catagory = Catagory.objects.all()
    context ={
        'all_catagory':all_catagory,
         
    }
    if request.method == 'POST':
        new_catagory = request.POST.get('catagory')
        add_new_catagory=Catagory.objects.create(Catagory_Name=new_catagory)
        if add_new_catagory:
            messages.success(request,"You have added a new category successfully.")
            return redirect('manage-catagory')
    return render(request,'Store_manager/Catagory/manage_catagory.html',context)
def add_new_catagory(request):
    all_catagory = Catagory.objects.all()
    context ={
        'all_catagory':all_catagory,
    }
    if request.method == 'POST':
        new_catagory = request.POST.get('catagory')
        total_item = request.POST.get('totalitem')
        add_new_catagory=Catagory.objects.create(Catagory_Name=new_catagory,total_item=total_item)
        print("-------")
        print(total_item)
        if add_new_catagory:
            messages.success(request,"You have added a new category successfully.")
    return render(request,'Store_manager/Catagory/manage_catagory.html',context)
def catagory_detail(request,id):
    catagory = Catagory.objects.get(pk=id)
    context={
        'catagory':catagory,
    }
    if request.method == 'POST':
        new_catagory = request.POST.get('catagory')
        catagory.Catagory_Name=new_catagory
        catagory.save()
        if catagory:
            messages.success(request,"You have update Category Name successfully.")
    return render(request,'Store_manager/Catagory/catagory_detail.html',context)
def delete_catagory(request,id):
    Catagory.objects.get(pk=id).delete()
    return redirect('manage-catagory')
def add_item(request,id):
    catagory=Catagory.objects.get(pk=id)
    context={
        'catagory':catagory
    }
    if request.method == 'POST':
        item_name = request.POST.get('itemname')
        amount = request.POST.get('total')
        new_item=Item.objects.create(Catagory=catagory,item_name=item_name,total_item_in_Stok=amount)
        if new_item:
            messages.success(request,"You have added New Item Successfully.")
            return redirect('catagory-detail' ,id)
    return render(request,'Store_manager/Catagory/catagory_detail.html',context)
def item_detail(request,id):
    item=Item.objects.get(pk=id)

    item_history=ItemHistory.objects.filter(Item=item)
    context={
        'item':item,
        'item_history':item_history,
    }
    if request.method == 'POST':
        new_catagory = request.POST.get('item_name')
        item.item_name=new_catagory
        item.save()
        if item:
            messages.success(request,"You have update item Name successfully.")
    return render(request,'Store_manager/Catagory/item_detail.html',context)
def item_delete(request,id):
    item=Item.objects.get(pk=id)
    catagory=item.Catagory
    id2=catagory.id
    Item.objects.get(pk=id).delete()
    return redirect('catagory-detail', id2)

def add_to_store(request):
    
    return render(request,"Store_manager/Add_to_Store/add_to_store.html")
def add_to_store1(request):
    if request.method == 'POST':
        res=request.POST.get('reson')
        
        all_item=Item.objects.all()
        all_orderd=form2permanent.objects.all()
        context={
            
            'res':res,
            'all_item':all_item,
            'all_orderd':all_orderd,

        }
        return render(request,"Store_manager/Add_to_Store/add_to_store1.html",context)
    return redirect('add-to-store')
   
def cheeck_request(request):
    return render(request,"Store_manager/cheeck_Request/cheeck_request.html")

def user_Profile(request):
    users = User.objects.get(id=request.user.id)
    admin = users.store_manager
    context= {
        'admin':admin,
    }
    return render(request,'Store_manager/profile/show_profile.html',context)

def edit_Profile(request):
    users = User.objects.get(id=request.user.id)
    admin = users.store_manager
    context= {
        'admin':admin,
    }
    if request.method == 'POST':
        admin.about = request.POST['about']
        admin.phone1 = request.POST['phone']
        admin.address = request.POST['address']
        admin.facebook = request.POST['facebook']
        admin.telegram = request.POST['telegram']
        admin.instagram = request.POST['instagram']
        users.first_name = request.POST['first_name']
        users.last_name = request.POST['last_name']
        users.email = request.POST['email']
        admin.save()
        users.save()
        messages.success(request,'Your profile has been updated successfully. ')
        return redirect('user-Profile')
    return render(request,'Store_manager/profile/edit_profile.html',context)

def chage_password(request):
    form = passwordform(request.user)
    if request.method == 'POST':
        form = passwordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('user-Profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = passwordform(request.user)
    context = {
        'form': form
        }
    return render(request,'Store_manager/profile/chage_pass.html',context)

def chage_profile_pic(request):
    users = User.objects.get(id=request.user.id)
    admin = users.store_manager
    context= {
        'admin':admin,
    }
    if len(request.FILES.get('newimg', "")) != 0:
        
        admin.profile_pic.delete()
        admin.profile_pic = request.FILES.get('newimg', "")
        admin.save()
        messages.success(request,'Your profile picture has been updated successfully.')
        return redirect('user-Profile')
    else:
        return render(request,'Store_manager/profile/change_profile_pic.html',context)

def delete_profile_pic(request):
    users = User.objects.get(id=request.user.id)
    admin = users.store_manager
    context= {
        'admin':admin,
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect('user-Profile')
    return render(request,)
def purchase(request):
   
    return render(request,'Store_manager/for_purchase/purchase.html')
def list_for_purchase(request):
    return render(request,'Store_manager/for_purchase/purchase_list.html',)
def new_action1(request):
    if form1temp.objects.all().count() !=0:
        print("already exist")
        all_form= form1temp.objects.all()
        form1=all_form[0]
        print(form1)
        print(all_form)
        form1temp.objects.all().delete()
        if request.method == 'POST':
            Request_by=request.POST.get('Request_by')
            Department=request.POST.get('Department')
            checked_by=request.POST.get('checkd_by')
            approved_by=request.POST.get('Approved_by')
            form1=form1temp.objects.create(Request_by=Request_by,Department=Department,checkd_by=checked_by, Approved_by=approved_by)
            if form1:
                messages.success(request,'You have sumite Form-1 successfuly.')
                return redirect('purchase')
    else:
        if request.method == 'POST':
            Request_by=request.POST.get('Request_by')
            Department=request.POST.get('Department')
            checked_by=request.POST.get('checkd_by')
            approved_by=request.POST.get('Approved_by')
            form1=form1temp.objects.create(Request_by=Request_by,Department=Department,checkd_by=checked_by, Approved_by=approved_by)
            if form1:
                messages.success(request,'You have sumite Form-1 successfuly.')
                return redirect('purchase')
    return render(request,'Store_manager/for_purchase/purchase.html')

def new_action(request):
    if request.method == 'POST':
        all_form= form1temp.objects.all()
        if all_form:
            form1=all_form[0]
            des=request.POST.get('desc')
            Qty=request.POST.get('qty')
            unit=request.POST.get('unit')
            remark=request.POST.get('remark')
            form2=form2temp.objects.create(form1=form1,Description=des,unit=unit,qty=Qty,Remark=remark)
            if form2:
                messages.success(request,'You have sumite Form-2 successfuly.')
                return redirect('purchase')
        else:
            messages.error(request,'First, you must complete and submit Form 1')
            return redirect('purchase')
def check_out(request):
    all_form= form1temp.objects.all()
    if all_form:
        form1=all_form[0]
        all_item=form2temp.objects.filter(form1=form1)
        if all_item:
            context={
                'form1':form1,
                'all_item':all_item,
            }
            return render(request,'Store_manager/for_purchase/check_out.html',context)
        else:
            messages.error(request,'First, you must complete and submit Form 2. ')
    else:
         messages.error(request,'First, you must complete and submit Form 1. ')
    return render(request,'Store_manager/for_purchase/purchase.html')


def list_for_purchase(request):
    all_list_item=form2permanent.objects.all().order_by('-id')
    context={
        'all_list_item':all_list_item,
    }
    all_form= form1temp.objects.all()
    if all_form:
        form1=all_form[0]
        all_item=form2temp.objects.filter(form1=form1)
        Request_by=form1.Request_by
        Department=form1.Department
        checkd_by=form1.checkd_by
        Approved_by=form1.Approved_by
        form1per=form1permanent.objects.create(Request_by=Request_by,Department=Department,checkd_by=checkd_by,Approved_by=Approved_by)
        if form1per:
            for item in all_item:
                Description=item.Description
                unit=item.unit
                qty=item.qty
                Remark=item.Remark
                form2permanent.objects.create(form1per=form1per,Description=Description,unit=unit,qty=qty,Remark=Remark)
                # messages.success(request,'You have submitted your purchase request successfully.')
                form1temp.objects.all().delete()
            messages.success(request,'You have submitted your purchase request successfully.')
                
    return render(request,'Store_manager/for_purchase/purchase_list.html',context)

def chat(request):
    return render(request,'Store_manager/chat/index.html')

def chat_pepol(request):
    return render(request,'Store_manager/chat/chat.html')

def report(request):
    return render(request,'Store_manager/Report/index.html')