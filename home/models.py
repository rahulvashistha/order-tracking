from django import utils
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.utils.timezone import now
from django.contrib.auth.models import User

#specify the choices
status_choices = (
    ("Order_received", "Order Received"),
    ("In_transit", "In Transit"),
    ("Out_for_delivery", "Out for Delivery"),
    ("Order_delivered", "Order Delivered"),
)
statustext_choices = (
    ("Your Order is Received", "Your Order is Received"),
    ("Your Order is In Transit", "Your Order is In Transit"),
    ("Your Order is Out for Delivery", "Your Order is Out for Delivery"),
    ("Your Order is Delivered", "Your Order is Delivered"),
)
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_Price = models.CharField(max_length=10)
    custname = models.CharField(max_length=50)
    custemail = models.CharField(max_length=50)
    custnumber = models.CharField(max_length=12)
    custaddress = models.CharField(max_length=100)
    order_Time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "OrderId: " + str(self.order_id) + " Added by: " + self.user.username

class Update(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE )
    update_Time = models.DateTimeField(auto_now=True, max_length=20)
    status = models.CharField(max_length=50, choices=status_choices, default="Order Received")
    statustext = models.CharField(max_length=50, choices=statustext_choices, default="Your Order is Received")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_id) + " Updated by: " + self.user.username + " At: " + str(self.update_Time)