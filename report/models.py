from django.db import models
from django.db.models.base import Model

class invoices(models.Model):
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length = 100)
    pay_method = models.CharField(max_length = 15)
    amount = models.FloatField(max_length=10)
    description = models.CharField(max_length=50)
    order_date = models.DateField()