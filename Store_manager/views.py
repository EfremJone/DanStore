from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, reverse
from .form import *
from .models import chatbot
from .models import *
from itertools import chain
from Department_Head.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import View
from Store_manager import models
from .process import html_to_pdf 
from django.core.exceptions import ObjectDoesNotExist

#Creating a class based view
def store_dashboard(request):
    id=(request.user.id)
    user=User.objects.get(id=id)
    re_emp=employ.objects.get(user=user)
    re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
    try:
        all_catagory = Catagory.objects.filter(store=re_Store)
    except Catagory.DoesNotExist:
        all_catagory = None
    context ={
        'all_catagory':all_catagory,
        're_emp':re_emp,
    }
    return render(request,'Store_manager/dashboard.html',context)

def manage_catagory(request):
    id=(request.user.id)
    user=User.objects.get(id=id)
    re_emp=employ.objects.get(user=user)
    re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
    try:
        all_catagory = Catagory.objects.filter(store=re_Store)
    except Catagory.DoesNotExist:
        all_catagory = None
    
    context ={
        'all_catagory':all_catagory,
         
    }
    if request.method == 'POST':
        new_catagory = request.POST.get('catagory')
        Type_of_Asset=request.POST.get('typeasset')
        new=Catagory.objects.filter(Catagory_Name=new_catagory)
        if new.count():
            
            messages.error(request,"A category name already exists. Please alter the category name.")
        else:
            add_new_catagory=Catagory.objects.create(store=re_Store,Catagory_Name=new_catagory,Type_of_Asset=Type_of_Asset)
            if add_new_catagory:
                messages.success(request,"You have added a new category successfully.")
                return redirect('manage-catagory')
    return render(request,'Store_manager/Catagory/manage_catagory.html',context)
def search_catagory(request):
    if request.method == 'POST':
        serched_catagory_name = request.POST.get('query')
        if serched_catagory_name:
            try:
                serched_catagory=Catagory.objects.get(Catagory_Name=serched_catagory_name)
                context={
              'serched_catagory':serched_catagory
            }
            except ObjectDoesNotExist:
                messages.error(request,"Please type the proper shelf name.")
                return redirect('store-dashboard')
                
            
            return render(request,'Store_manager/Catagory/search_catagory.html',context)
        else:
            messages.error(request,"Please enter shelf name")
            return redirect('store-dashboard')
    
    return render(request,'Store_manager/Catagory/search_catagory.html',context)
def add_new_catagory(request):
    all_catagory = Catagory.objects.all()
    context ={
        'all_catagory':all_catagory,
    }
    if request.method == 'POST':
        new_catagory = request.POST.get('catagory')
        total_item = request.POST.get('totalitem')
        add_new_catagory=Catagory.objects.create(Catagory_Name=new_catagory,total_item=total_item)
        
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


def add_to_store1(request):
    id=(request.user.id)
    user=User.objects.get(id=id)
    re_emp=employ.objects.get(user=user)
    re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
    try:
        all_catagory = Catagory.objects.filter(store=re_Store)
        all_emp=employ.objects.filter(accessStore=re_Store)
    except Catagory.DoesNotExist:
        all_catagory = None
   
    
    if request.method == 'POST':
        res=request.POST.get('reson')
        all_item=Item.objects.all()
        all_orderd=form2permanent.objects.all()
        requ_by_dept_recv=dept_request_form1_permanent.objects.filter (Q(request_store=re_Store) & Q(Recival_status_by_Employer="Received")).order_by("-id") 
        requ_by_emp_recv=employe_request_form1_permanent.objects.filter(Q(request_store=re_Store) & Q(Recival_status_by_Employer="Received")).order_by("-id") 
        all_receved_req=list(chain(requ_by_dept_recv, requ_by_emp_recv))
    
        context={
            
            'res':res,
            'all_item':all_item,
            'all_orderd':all_orderd,
            'all_catagory':all_catagory,
            'all_emp':all_emp,
            'all_receved_req':all_receved_req,

        }
  
        
        return render(request,"Store_manager/Add_to_Store/add_to_store1.html",context)
    return redirect('add-to-store')
   
def cheeck_request(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    name=exploreU.Full_Name
    store=allStore.objects.get(storeKeeper=name)
    emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    all_unreseved_req=list(chain(emp_request, dep_request))
    context={
        'emp_request':all_unreseved_req
    }
    return render(request,"Store_manager/cheeck_Request/cheeck_request.html",context)

def aproved_request(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    name=exploreU.Full_Name
    store=allStore.objects.get(storeKeeper=name)
    emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    all_unreseved_req=list(chain(emp_request, dep_request))
    context={
        'emp_request':all_unreseved_req
    }
    return render(request,'Store_manager/cheeck_Request/approved_request.html',context)

def rejected_request(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    name=exploreU.Full_Name
    store=allStore.objects.get(storeKeeper=name)
    emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    all_unreseved_req=list(chain(emp_request, dep_request))
    context={
        'emp_request':all_unreseved_req
    }
    return render(request,'Store_manager/cheeck_Request/rejected_request.html',context)

def check_in_stok(request,Description):
    req_item_inlower=Description.lower()
    req_item_inupper=Description.capitalize()
    try: 
        order_item=Item.objects.filter(item_name=req_item_inlower)
    except ObjectDoesNotExist:
        try:
            order_item=Item.objects.filter(item_name=req_item_inupper)
        except ObjectDoesNotExist:
            order_item=None
    print(order_item)
    for item in order_item: 
        print(item.item_name)
    context={
           'order_item':order_item
    }
    return render(request,'Store_manager/cheeck_Request/check_in_soke.html',context)
def put_message_rejected_request(request,id):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    name=exploreU.Full_Name
    store=allStore.objects.get(storeKeeper=name)
    emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    all_unreseved_req=list(chain(emp_request, dep_request))
    for requ in all_unreseved_req:
        if requ.id==id:
            searchedReq=requ
            print(searchedReq)
    context={
        'searchedReq':searchedReq,
    }
    
    if request.method == 'POST':
        mess=request.POST.get('store_message')
        id=str(request.POST.get('request_id'))
        for requ in all_unreseved_req:
            if str(requ.id)==id:
                searchedReq=requ
                searchedReq.note=mess
                searchedReq.Store_Keeper_Action="Reject"
                searchedReq.save()
                return redirect('rejected-request')
    return render(request,"Store_manager/cheeck_Request/message1.html",context)

def send_message_to_request(request,id):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    name=exploreU.Full_Name
    store=allStore.objects.get(storeKeeper=name)
    emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    all_unreseved_req=list(chain(emp_request, dep_request))
    for requ in all_unreseved_req:
        if requ.id==id:
            searchedReq=requ
            print(searchedReq)
    context={
        'searchedReq':searchedReq,
    }
    
    return render(request,"Store_manager/cheeck_Request/message.html",context)
def store_manage_approve(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    name=exploreU.Full_Name
    store=allStore.objects.get(storeKeeper=name)
    emp_request=employe_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    dep_request=dept_request_form1_permanent.objects.filter(Q(request_store=store) & Q(dept_head_Action="Approved"))
    all_unreseved_req=list(chain(emp_request, dep_request))
    
    if request.method == 'POST':
        mess=request.POST.get('store_message')
        id=str(request.POST.get('request_id'))
        for requ in all_unreseved_req:
            if str(requ.id)==id:
                searchedReq=requ
                searchedReq.note=mess
                searchedReq.Store_Keeper_Action="Allowed"
                searchedReq.save()
                return redirect('aproved_request')


    return render(request,"Store_manager/cheeck_Request/message.html")
def user_Profile(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    context= {
        'admin':admin,
    }
    return render(request,'Store_manager/profile/show_profile.html',context)

def edit_Profile(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
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
    re_employ=employ.objects.get(user=users)
    admin = re_employ
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
    re_employ=employ.objects.get(user=users)
    admin = re_employ
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
        all_form= form1temp.objects.all()
        form1=all_form[0]
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
            form2=form2temp.objects.create(form1=form1,Description=des,unit=unit,req_qty=Qty,Remark=remark)
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
                qty=item.req_qty
                Remark=item.Remark
                form2permanent.objects.create(form1per=form1per,Description=Description,unit=unit,req_qty=qty,Remark=Remark)
                # messages.success(request,'You have submitted your purchase request successfully.')
                form1temp.objects.all().delete()
            messages.success(request,'You have submitted your purchase request successfully.')
                
    return render(request,'Store_manager/for_purchase/purchase_list.html',context)

def chat(request):
    chat_team=[]
    chat_team1=[]
    chat_group=employ.objects.all()
    # all_chat_team=chatbot.objects.filter()
    user=User.objects.get(pk=request.user.id)
    me=employ.objects.get(user=user)
    all_message=chatbot.objects.filter(Q(me_with=me) | Q(me=me))
    # result = any(item in test_list for item in test_list)
    for team in all_message:
        if (Q(team.me_with) | Q(team.me))  in chat_team:
            pass
        else:
            chat_team.append(team.me_with)
            

    
    for a in chat_team:
        chat_group1=employ.objects.get(pk=a.id)
    
   
    if request.method == 'POST':
        user=request.POST.get('serach')
        serch=User.objects.get(username=user)
        chat_group1=employ.objects.get(user=serch)
   
        context={
            
            'chat_group1':chat_group,
        }
        return render(request,'Store_manager/chat/index1.html',context)

    context={
            'chat_group':chat_group,
            
        }
    return render(request,'Store_manager/chat/index.html',context)

def chat_pepol(request,id):
    chat_employ=employ.objects.get(pk=id)
    user=User.objects.get(pk=request.user.id)
    me=employ.objects.get(user=user)
   
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

def chat_profile(request,id):
    chat_employ=employ.objects.get(pk=id)
    context={
        'chat_employ':chat_employ,
    }
    return render(request,'Store_manager/chat/profile.html',context)
def send_message(request):
    me=request.user
    if request.method == 'POST':
        pass
    return redirect('chat_pepol')
def report(request):
    
    return render(request,'Store_manager/Report/index.html',)



def add_to_store(request):
    id=(request.user.id)
    user=User.objects.get(id=id)
    re_emp=employ.objects.get(user=user)
    re_Store=allStore.objects.get(storeKeeper=re_emp.Full_Name)
    try:
        all_catagory = Catagory.objects.filter(store=re_Store)
    except Catagory.DoesNotExist:
        all_catagory = None
    
    context ={
        'all_catagory':all_catagory,
        
    }
    if request.method == 'POST':
        Reseaon = request.POST.get('res')
        if (Reseaon=='Gift'):
            pass
        elif (Reseaon=='Purchased'):
            OrderId= request.POST.get('OrderId')
            item_name= request.POST.get('item_name')
            
            print("this is item name",item_name)
            
            Qty= int(request.POST.get('Qty'))
            catagory= request.POST.get('catagory_name')
           
            print("This is catagory name",catagory)
            
            item=form2permanent.objects.get(id=OrderId)
            item.add_qty=item.add_qty+Qty
           
            if (item.req_qty-item.add_qty==0):
                item.Status="Completed"
                cat=Catagory.objects.get(Catagory_Name=catagory)
                if cat.Type_of_Asset=="Fixed assets":
                    new_item=Item.objects.create(
                    store=re_Store,
                    Catagory=cat,
                    Order_Id=OrderId,
                    item_name=item_name,
                    Reason='Purchased',
                    total_item_in_Stok= item.add_qty,
                    add_by=re_emp,
                    Action='New_Add',
                    )
                    if new_item:
                        print("new item added")
                elif cat.Type_of_Asset=="Current assets":
                    print("this is Current assets")
                else:
                    print("not assiged")
                
            elif(item.req_qty>item.add_qty):
                item.Status="Pending"
                # new_item=Item.objects.create(
                # store=re_Store,
                # Catagory=catagory,
                # Order_Id=OrderId,
                # item_name=item_name,
                # Reason='Purchased',
                # total_item_in_Stok= item.add_qty,
                # add_by=re_emp,
                # Action='New_Add',
                # )
                # if new_item:
                #     print("new item added")
            elif(item.req_qty<item.add_qty):
                item.add_qty=item.add_qty-Qty
                messages.error(request,'Sorry, the data you entered is not valid.')
                return redirect('list_for_purchase')
            item.save()
            
        elif (Reseaon=='Other'):
            pass
        elif (Reseaon=='Returned'):
            pass
       
        return redirect('list_for_purchase')
    return render(request,"Store_manager/Add_to_Store/add_to_store.html",context)
def add_to_store_by_return(request):
    
    if request.method == 'POST':
        name_id=int(str(request.POST.get('name')))
        Description=str(request.POST.get('item'))
        qty=int(str(request.POST.get('qty')))
    req_item_inlower=Description.lower()
    req_item_inupper=Description.capitalize()
    try: 
        ret_item=Item.objects.get(item_name=req_item_inlower)
    except ObjectDoesNotExist:
        try:
            ret_item=Item.objects.get(item_name=req_item_inupper)
        except ObjectDoesNotExist:
            ret_item=None
    ret_emp=employ.objects.get(id=name_id)
    Request_by=ret_emp.Full_Name
    current_instok=int(ret_item.total_item_in_Stok)
    updated=current_instok + qty
    ret_item.total_item_in_Stok=str(updated)
    ret_item.save()

    ItemHistory.objects.create(Item=ret_item,Reason='Returned Material',Action='Add',Amount=qty)
    returend_item=employe_request_form1_permanent.objects.get(Q(Request_by=Request_by) & Q(Description=Description))
    returend_item.Recival_status_by_Employer='Returned'
    returend_item.save()
    return redirect('item_detail', ret_item.id)
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



class GeneratePdf(View):
   def get(self, request, *args, **kwargs):
    all_form= form1temp.objects.all()
    if all_form:
        form1=all_form[0]
        all_item=form2temp.objects.filter(form1=form1)
        data={
            'form1':form1,
            'all_item':all_item,
        }
        open('templates/temp.html', "w").write(render_to_string('Store_manager/for_purchase/invoce.html',data ))
        pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')