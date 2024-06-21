from django.db import models
from users.models import Users
from shop.models import Product
from django.core.validators import MinValueValidator


class Cart(models.Model):

    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(1, "Minimum quantity is one")])

    class Meta:
        unique_together = ['username','product']
        
    def __str__(self):
        return f"{self.product} ({str(self.username)})"
