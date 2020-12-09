from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROFILE_STATUS = (
    (1,"MSEGS"),
    (2,"SUPPLIER"),
    (3,"DISTRICT")
)
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profile_status = models.IntegerField(choices=PROFILE_STATUS,default=3)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    supplier_code = models.CharField(max_length=255,null=True)


    name = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    address2 = models.CharField(max_length=255,null=True)
    postal_code = models.IntegerField(default=0,null=True)
    phone_number = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name

class District(models.Model):
    district = models.CharField(max_length=255,null=True)
    manager = models.ForeignKey(Profile, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.district

class Category(models.Model):
    name= models.CharField(max_length=255)
    category_code= models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
        
STATUS_CHOICES = (
    (1,"ACTIVE"),
    (2,"IDLE"),
    (3,"REPAIR")
)

PROCESS_CHOICES = ((1,"ACTIVE"),(2,"IN PROCESS"))

class Item(models.Model):
    name = models.CharField(max_length=200,null=True)
    category = models.ForeignKey(Category, related_name='category',null=True, blank=True,on_delete=models.CASCADE)
    # status = models.IntegerField(default=1)
    district = models.ForeignKey(District, null=True, blank=True,on_delete=models.SET_NULL)
    status = models.IntegerField(choices=STATUS_CHOICES,default=2)
    process = models.IntegerField(choices=PROCESS_CHOICES,default=1)
    item_code = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.name

    
    



# class ItemInfo(models.Model):
#     item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
#     Manufacturer = models.CharField(max_length=255)
#     colours =models.CharField(max_length=255)

#     def __str__(self):
#         return self.item

class Request(models.Model):
    created = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    remarks = models.TextField(blank=True)
    initiator = models.ForeignKey(District,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False,null=True)

    def __str__(self):
        return f'{self.item} by {self.initiator}'

class Transaction(models.Model):
    items = models.ManyToManyField(Request)
    initiator = models.ForeignKey(District,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)#Approval by state admin
    accepted = models.BooleanField(default=False)#For District 1
    completed = models.BooleanField(default=False)#For Dest District

    def __str__(self):
        return f'{self.initiator}'

class Order(models.Model):
    items = models.TextField(blank=True)
    accepted_status = models.BooleanField(default=False)#Is accepted by District 1 
    completed = models.BooleanField(default=False)#Is received by District 2

class Reallocation(models.Model):
    created = models.DateTimeField(auto_now_add=True,null=True)
    item = models.OneToOneField(Item,on_delete=models.CASCADE)
    initiator = models.ForeignKey(District,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)#Approval by state admin
    accepted = models.BooleanField(default=False)#For District 1
    completed = models.BooleanField(default=False)#For Dest District


    # current_holder = models.ForeignKey(District,on_delete=models.CASCADE,null=True,related_name='current_holder')

    # def save(self, *args, **kwargs):
    #     i = self.item.district
    #     self.current_holder = i
    #     super(Reallocation,self).save(*args, **kwargs)

    current= models.ForeignKey(District,on_delete=models.CASCADE,null=True,related_name='current',blank=True)

    def save(self, *args, **kwargs):
        i = self.item.district
        self.current = i
        super(Reallocation,self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.item} (from {self.current} to {self.initiator})'
class Manufacturer(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f'{self.name}'

class ItemInfo(models.Model):
    item = models.OneToOneField(Item,null=True,on_delete = models.SET_NULL)
    item_code = models.CharField(max_length=255,null=True,blank=True)
    manufacturer = models.ForeignKey(Manufacturer,null=True,on_delete=models.SET_NULL)
    colour = models.CharField(max_length=255,null=True,blank=True)
    purchased_date = models.DateTimeField(auto_now=True,blank=True)
    purchased_price = models.FloatField(blank=True,null=True,default=0.0)
    depreciation = models.FloatField(blank=True,null=True,default=0.0)
    salvage_value = models.FloatField(blank=True,null=True,default=0.0)
    useful_life = models.IntegerField(blank=True,null=True)
    def save(self, *args, **kwargs):
        self.depreciation = (self.purchased_price - self.salvage_value)/self.useful_life
        super(ItemInfo,self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.item}'