from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.DecimalField(default=0, max_length=100, max_digits=5, decimal_places=2, validators=[
                                MinValueValidator(0, "Can not be in negative"),MaxValueValidator(100,"Can not be more than 100")])

    def __str__(self):
        return self.name
