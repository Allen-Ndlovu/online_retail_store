from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self): return self.name

class Product(models.Model):
    name        = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    stock       = models.PositiveIntegerField()
    category    = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    rating      = models.FloatField(default=0.0)
    description = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['-rating']),
        ]

    def __str__(self): return self.name
