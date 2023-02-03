from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import *
def finance_view(request):
    all_list_item=form2permanent.objects.all()
    
    context={
        'all_list_item':all_list_item,
    }
    return render(request,'Finance/index.html',context)
def finance_respons(request,id):
    req_order=form2permanent.objects.get(pk=id)
    context={
        'req_order':req_order,
    }
    if 'approve' in request.POST:
        note=request.POST.get('note')
        req_order.Finance_response=note
        req_order.Finance_Action='Completed'
        req_order.save()
        return redirect('finance_dashboard')
    
    return render(request,'Finance/finance_respons.html',context)