from django.contrib.auth.models import User
from shops.models import MagazaUrunu,UrunKategorisi
from django.db import models
# Create your models here.





    
    
    
    
    
 
 #https://stackoverflow.com/questions/68591501/models-foreignkey-in-django
 #https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/
 
class ShippingAdress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)#
    email = models.EmailField()#
    phone = models.CharField(max_length=264)   # bu yok 
    adress = models.TextField()#
    city = models.CharField(max_length=264)#

    zip = models.CharField(max_length=264)#

    
    def __str__(self):
        return  'adress ' + str(self.id)
    
    
    #class Meta
    class Meta:
        verbose_name_plural = 'ShippingAdresses'
        
        
        
        
        
        
        
        
        
#order
class CustomerOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)  # Allow null values
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    delivery_address = models.TextField()
    paid = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    order_date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username if self.customer else 'Anonymous'}"

    class Meta:
        verbose_name_plural = 'Customer Orders'


class OrderDetail(models.Model):
    customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='order_items', null=True)
    product = models.ForeignKey(MagazaUrunu, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Detail {self.id} for Order {self.customer_order.id}"
