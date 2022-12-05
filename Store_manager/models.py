from django.db import models

# Create your models here.

class Catagory(models.Model):
    Catagory_Name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.Catagory_Name)

class Item(models.Model):
    Catagory =models.ForeignKey(Catagory,null=True, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200,null=True,blank=True)
    total_item_in_Stok = models.CharField(max_length=200, null=True, blank=True, default="0")
    last_update=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.Catagory) + str('|') + str(self.id) 

class ItemHistory(models.Model):
    action_choice=(
        ('New_Add','New_Add'),
        ('Removed','Removed'),
    )
    Item=models.ForeignKey(Item,null=True,blank=True, on_delete=models.CASCADE)
    Reason=models.CharField(max_length=200,blank=True,null=True)
    Action=models.CharField(max_length=200,choices=action_choice)
    Approved=models.CharField(max_length=200,blank=True,null=True)
    last_update=models.DateField(auto_now_add=True)


class form1temp(models.Model):
    Request_by=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    checkd_by=models.CharField(max_length=100,null=True,blank=True)
    Approved_by=models.CharField(max_length=100,null=True,blank=True)
class form2temp(models.Model):
    form1=models.ForeignKey(form1temp,null=True,blank=True, on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    qty=models.CharField(max_length=100,null=True,blank=True)
    Remark=models.CharField(max_length=100,null=True,blank=True)

class form1permanent(models.Model):
    Request_by=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    checkd_by=models.CharField(max_length=100,null=True,blank=True)
    Approved_by=models.CharField(max_length=100,null=True,blank=True)
class form2permanent(models.Model):
    status=(
        ('Pending','Pending'),
        ('Accepte','Accepte'),
        
    )
    form1=models.ForeignKey(form1temp,null=True,blank=True, on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    qty=models.CharField(max_length=100,null=True,blank=True)
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
    qty=models.CharField(max_length=100,null=True,blank=True)
    Status=models.CharField(max_length=200,null=True,blank=True,choices=status,default="Pending")
    date=models.DateField(auto_now_add=True,null=True)
    Remark=models.CharField(max_length=100,null=True,blank=True)

class student(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)