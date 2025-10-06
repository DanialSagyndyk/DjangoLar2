# Django Modules
from django.db import models
from django.coutrib.auth.models import User
from catalogs.models import MenuItem, Restaurant


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    apartment = models.CharField(max_length=20, blank=True, null=True)
    comment = models.TextField(blank=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.house}"


class PromoCode(models.Model):
    code = `models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.code


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('delivering', 'Delivering'),
        ('done' 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    promo_code = models.ManyToManyField(PromoCode, through='OrderPromoCode', blank=True)  
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

    
class OrderItemOption(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='options')
    option = models.ForeignKey('catalogs.Option', on_delete=models.CASCADE)
    additional_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.order_item.menu_item.name}"


class OrderPromoCode(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.promo_code.code} for Order {self.order.id}"

        