from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class allStore(models.Model):
    storeName= models.CharField(max_length=300,null=False, blank=False)
    storeDescription = models.TextField(null=False,blank=False)
    storeKeeper = models.CharField(max_length=300,null=False,blank=False)
    storeLocation = models.TextField(null=False,blank=False)
    def __str__(self) -> str:
        return str(self.storeName)
        
class Catagory(models.Model):
    Catagory_Name = models.CharField(max_length=200, null=True, blank=True)
    store=models.ForeignKey(allStore,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Catagory_Name)

class form1temp(models.Model):
    date=models.DateField(auto_now_add=True,null=True)
    Request_by=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    checkd_by=models.CharField(max_length=100,null=True,blank=True)
    Approved_by=models.CharField(max_length=100,null=True,blank=True)
class form2temp(models.Model):
    form1=models.ForeignKey(form1temp,null=True,blank=True, on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    req_qty=models.CharField(max_length=100,null=True,blank=True)
    add_qty=models.CharField(max_length=100,null=True,blank=True,default="0")
    Remark=models.CharField(max_length=100,null=True,blank=True)

class form1permanent(models.Model):
    date=models.DateField(auto_now_add=True,null=True)
    Request_by=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    checkd_by=models.CharField(max_length=100,null=True,blank=True)
    Approved_by=models.CharField(max_length=100,null=True,blank=True)
class form2permanent(models.Model):
    status=(
        ('Pending','Pending'),
        ('Completed','Completed'),
        
    )
    form1=models.ForeignKey(form1temp,null=True,blank=True, on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    req_qty=models.CharField(max_length=100,null=True,blank=True)
    add_qty=models.CharField(max_length=100,null=True,blank=True,default="0")
    Status=models.CharField(max_length=200,choices=status,default='Pending')
    Remark=models.CharField(max_length=100,null=True,blank=True)

class form2permanent(models.Model):
    status=(
        ('Pending','Pending'),
        ('Accepte','Accepte'),
    )
    form1per=models.ForeignKey(form1permanent,null=True,blank=True, on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    req_qty=models.IntegerField(null=True,blank=True)
    add_qty=models.IntegerField(null=True,blank=True)
    Status=models.CharField(max_length=200,null=True,blank=True,choices=status,default="Pending")
    date=models.DateField(auto_now_add=True,null=True)
    Remark=models.CharField(max_length=100,null=True,blank=True)

class department(models.Model):
    departmentName = models.CharField(max_length=100, null=False)
    departmentDescription = models.TextField(max_length=500, null=False)
    departmentHead = models.CharField(max_length=40, null=False)
    def __str__(self) -> str:
        return str(self.departmentName)

class allRole(models.Model):
    roleName = models.CharField(max_length=100,null=False)
    roleMembers = models.IntegerField(null=False, blank=False)
    roleDetails = models.TextField(null=True,blank=True)
    def __str__(self)-> str:
        return str(self.roleName)

class employ(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    role= models.CharField(max_length=200,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    Full_Name=models.CharField(max_length=300, null=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True,blank=True)
    telegram = models.CharField(max_length=200, null=True,blank=True)
    instagram = models.CharField(max_length=200, null=True,blank=True)
    about = models.TextField(max_length=500, null=True)
    address = models.CharField(max_length=200, null=True)
    inDepartment = models.ForeignKey(department,max_length=300,null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    accessStore=models.ForeignKey(allStore,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
class chatbot(models.Model):
    me_with=models.ForeignKey(employ,null=True,blank=True, on_delete=models.CASCADE)
    me=models.CharField(max_length=200,null=True,blank=True)
    message=models.TextField(max_length=1000,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    checked=models.BooleanField(default=False)
    def __str__(self):
        return str(self.date)



class vendor(models.Model):
    vendorCode = models.AutoField(primary_key=True)
    vendorName = models.CharField(max_length=300,null=False)
    vendorProducts = models.CharField(max_length=300, null=False)
    vendorOrigin = models.CharField(max_length=300,null=False)
    vendorType = models.CharField(max_length=300,null=False)
    vendorAdded = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.vendorName)



class Item(models.Model):
    action_choice=(
        ('New_Add','New_Add'),
        ('Removed','Removed'),
    )
    Add_Reason=(
        
        ('Returned Material','Returned Material'),
        ('Gift','Gift'),
        ('Purchased','Purchased'),
        ('Other','Other'),
    )
    store=models.ForeignKey(allStore,null=True, on_delete=models.CASCADE)
    Catagory =models.ForeignKey(Catagory,null=True, on_delete=models.CASCADE)
    Order_Id =models.CharField(max_length=200,null=True,blank=True)
    item_name=models.CharField(max_length=200,null=True,blank=True)
    vender=models.CharField(max_length=200,null=True,blank=True)
    serial_No=models.CharField(max_length=200,null=True,blank=True)
    Reason=models.CharField(max_length=200,blank=True,null=True,choices=Add_Reason)
    Action=models.CharField(max_length=200,null=True,choices=action_choice)
    Approved=models.CharField(max_length=200,blank=True,null=True)
    created_date=models.DateField(auto_now_add=True,null=True)
    unit=models.CharField(max_length=200,null=True,blank=True)
    total_item_in_Stok = models.CharField(max_length=200, null=True, blank=True, default="0")
    add_by=models.CharField(max_length=200,null=True,blank=True)
    return_by=models.CharField(max_length=200,null=True,blank=True)
    last_update=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.Catagory) + str('|') + str(self.id) 

class ItemHistory(models.Model):
    action_choice=(
        ('New_Add','New_Add'),
        ('Removed','Removed'),
    )
   
    Add_Reason=(
        
        ('Returned Material','Returned Material'),
        ('Gift','Gift'),
        ('Purchased','Purchased'),
        ('Other','Other'),
    )
    
    Item=models.ForeignKey(Item,null=True,blank=True, on_delete=models.CASCADE)
    Reason=models.CharField(max_length=200,blank=True,null=True,choices=Add_Reason)
    Action=models.CharField(max_length=200,choices=action_choice)
    Approved=models.CharField(max_length=200,blank=True,null=True)
    last_update=models.DateField(auto_now_add=True)