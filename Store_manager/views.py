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
def item_detail(request):
    return render(request,'Store_manager/Catagory/item_detail.html')
def add_to_store(request):
    return render(request,"Store_manager/Add_to_Store/add_to_store.html")
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
