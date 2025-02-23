from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = [
    ('ap','apple'),
    ('sm','samsung'),
    ('on','oneplus'),
    ('v','vivo'),
    ('n','nothing'),
    ('la','lava'),
    ('op','oppo'),


]
class Mobile(models.Model):
    name = models.TextField(max_length=100) 
    company = models.TextField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.TextField(choices=CATEGORY)
    specs = models.TextField()
    description = models.TextField()
    upload_image = models.ImageField(upload_to='product/',default='')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_data():
        return Mobile.objects.all()

MONITOR_CATEGORY = [
    ('sm','Samsung'),
    ('ac','Accer'),
    ('ms','MSI'),
    ('ap','Apple'),
    ('gb','Gigabyte'),
    ('ln','Lenovo'),
    ('lg','LG'),

]
    
class Monitor(models.Model):
    name = models.TextField(max_length=100) 
    company = models.TextField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField()
    monitorcategory = models.TextField(choices=MONITOR_CATEGORY)
    specs = models.TextField()
    description = models.TextField()
    upload_image = models.ImageField(upload_to='product/',default='')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def monitors():
        return Monitor.objects.all()

EARPHONES_CATEGORY = [
    ('sm','Samsung'),
    ('rm','Realme'),
    ('tr','truke'),
    ('bt','Boat'),
    ('mv','Mivi'),
    ('ap','Apple'),
    ('ns','Noise'),
    ('blt','Bolt'),
]
class Earphone(models.Model):
    name = models.TextField(max_length=100) 
    company = models.TextField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField()
    earphonescategory = models.TextField(choices=EARPHONES_CATEGORY)
    specs = models.TextField()
    description = models.TextField()
    upload_image = models.ImageField(upload_to='product/',default='')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def earphones():
        return Earphone.objects.all()
    

GAMINGCONSOL_CATEGORY = [
    ('ps3','Playstation3'),
    ('ps4','Playstation4'),
    ('ps5','Playstation5'),
    ('xb','Xbox360'),
    ('xb','XboxSeriesX'),
    ('xb','XboxSeriesS'),
   
]
class GamingConsole(models.Model):
    name = models.TextField(max_length=100) 
    company = models.TextField(max_length=100)
    price = models.FloatField()
    discounted_price = models.FloatField()
    earphonescategory = models.TextField(choices=GAMINGCONSOL_CATEGORY)
    specs = models.TextField()
    description = models.TextField()
    upload_image = models.ImageField(upload_to='product/',default='')
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def consoles():
        return GamingConsole.objects.all()







STATE_CHOICES = [
    ('dl','Delhi'),
    ('mp','Madhya Pradesh'),
    ('ml','Maldives'),
    ('bn','Bankok'),
    ('cp','Canaught Place '),

]
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100,default="")
    city = models.CharField(max_length=100)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)

    def __str__(self):
        return self.name
    
GAMESCATEGORY = [
    ('GodOfWar','GofOfWar'),
    ('AlanWake','AlanWake'),
    ('WatchDogs2','WatchDogs2'),
    ('RDR2','RDR2'),
    ('GTA 5','GTA5'),
    ('GTA 6','GTA6'),
    ('BlackMythwukon','Blckmythwukong'),
]
class Games(models.Model):
    name =  models.TextField()
    Company =  models.TextField()
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    description = models.TextField()
    gamecategory = models.TextField(choices=GAMESCATEGORY,default="")
    upload_image = models.ImageField(upload_to='product/',default='')

    def __str__(self):
        return self.name
    
    @staticmethod
    def mygames():
        return Games.objects.all()
    

    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)




STATUS_CHOICES = (
    ('Order placed','Order placed'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Mobile,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
   



