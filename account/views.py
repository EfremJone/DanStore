from django.shortcuts import render

# Create your views here.


def log_in(request):
    return render(request,'account/login.html',{})