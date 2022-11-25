from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from .form import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect


def store_dashboard(request):
    return render(request,'Store_manager/dashboard.html')
def manage_catagory(request):
    return render(request,'Store_manager/Catagory/manage_catagory.html')
def add_to_store(request):
    return render(request,"Store_manager/Add_to_Store/add_to_store.html")
def cheeck_request(request):
    return render(request,"Store_manager/cheeck_Request/cheeck_request.html")
def user_Profile(request):
    return render(request,'Store_manager/profile/show_profile.html')
def edit_Profile(request):
    return render(request,'Store_manager/profile/edit_profile.html',)
def chage_password(request):
    if request.method == 'POST':
        form = passwordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('show_profile_agent')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = passwordform(request.user)
        context = {
            'form': form
            }
    return render(request,'Store_manager/profile/chage_pass.html',context)

def chage_profile_pic(request):
    return render(request,'Store_manager/profile/change_profile_pic.html')