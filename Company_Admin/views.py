from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,'Admin/Dashboard/index.html')

def manage_employee(request):
    return render(request,'Admin/ManageEmployee/index.html')

def departments(request):
    return render(request,'Admin/Departments/index.html')

def vendors(request):
    return render(request,'Admin/Vendors/index.html')

def role(request):
    return render(request,'Admin/Role/index.html')

def products(request):
    return render(request,'Admin/Products/index.html')

def store(request):
    return render(request,'Admin/Store/index.html')

def batch(request):
    return render(request,'Admin/Batch/index.html')

def reports(request):
    return render(request,'Admin/Reports/index.html')

def chat(request):
    chat_group=employ.objects.all()
    context={
      
        'chat_group':chat_group,
    }
    return render(request,'Store_manager/chat/index.html',context)

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
            return redirect('chat_pepol',id)
    context={
        'chat_employ':chat_employ,
        'message':all_message,
        'id':id,
        'me':me
    }
    return render(request,'Store_manager/chat/chat.html',context)
def send_message(request):
    me=request.user
    if request.method == 'POST':
        print(me)

    return redirect('chat_pepol')