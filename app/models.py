from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
class Decoration(models.Model):

    Customer_Name = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    decofor = models.CharField(max_length=50,null=True)
    flat = models.CharField(max_length=50,null=True)
    cleaning = models.CharField(max_length=50,null=True)
    materials = models.CharField(max_length=50,null=True)
    

class Book_Deco(models.Model):
    
    Cust_Name = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    
    
    
class Babysitter(models.Model):
    Customer_Name = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=10)
    babymess = models.CharField(max_length=1000)
    