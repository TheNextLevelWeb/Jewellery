from django.db import models
from shop.models import Product
from users.models import Users
from django.core.exceptions import ValidationError

class Rating(models.Model):
    rating_choices = {
        1:"Very poor",
        2:"Poor",
        3:"Average",
        4:"Good",
        5:"Execellent",
    }
    product = models.ForeignKey(
        Product, to_field='name', on_delete=models.CASCADE)
    username = models.ForeignKey(Users,to_field='username',on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices,null=False)
    review = models.TextField(blank=False)

    class Meta:
        unique_together = ('product', 'username')
        
    def __str__(self):
        return f"{self.product}'s rating by {self.username}"