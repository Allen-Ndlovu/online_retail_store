from django.db import models
from django.contrib.auth.models import User
from core.models import Product

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING    = 'PENDING'
        PROCESSING = 'PROCESSING'
        COMPLETED  = 'COMPLETED'
        CANCELLED  = 'CANCELLED'

    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    status  = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product  = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
