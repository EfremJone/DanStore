from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user,'groups'):
                a = request.user.groups.all()[0].name
                if a == 'Admin':
                    return redirect('admin-dashboard')   
                elif a == 'Store_Manager':
                     return redirect('store-dashboard',)
        else:
            messages.error(request,'You are not authenticated')
            return render(request, 'Account/login.html')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            print(password)
            
            user = authenticate(username=username, password=password)
            
            if hasattr(user,'groups'):
                    a = user.groups.all()[0].name
                    if a == 'Admin':
                        login(request, user)
                        return redirect('admin-dashboard')
                    elif a == 'Store_Manager':
                        login(request, user)
                        return redirect('store-dashboard',)
            else:
                messages.error(request,'Username or password is not correct!')
                return render(request, 'account/login.html')
    return render(request, 'account/login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('login')

