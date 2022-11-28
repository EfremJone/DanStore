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
        return str(self.Catagory) + str('|') + str(self.item_name) 
