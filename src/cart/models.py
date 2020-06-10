from django.db import models
from userprofile.models import Profile
from products.models import Product
# Create your models here.

class OrderItem(models.Model):
    owner           = models.ForeignKey(Profile , on_delete=models.CASCADE)
    product         = models.ForeignKey(Product , on_delete=models.SET_NULL ,null = True)
    is_ordered      = models.BooleanField(default=False)
    date_added      = models.DateTimeField(auto_now=True)
    date_ordered    = models.DateTimeField(null=True)

    objects         = models.Manager()

    def __str__(self):
        return self.product.name


class Order(models.Model):
    owner           = models.ForeignKey(Profile , on_delete=models.SET_NULL , null = True)
    is_ordered      = models.BooleanField(default=False)
    items           = models.ManyToManyField(OrderItem)
    date_ordered    = models.DateTimeField(auto_now=True)

    objects         = models.Manager()

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()]) 

    def __str__(self):
        return self.owner.name + "  \t  " + self.owner.user.email


class Transaction(models.Model):
    profile     = models.ForeignKey(Profile , on_delete=models.SET_NULL , null= True)
    order_id    = models.CharField(max_length=120)
    amount      = models.DecimalField(max_digits=64, decimal_places=2)
    success     = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True )

    objects = models.Manager()

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']



