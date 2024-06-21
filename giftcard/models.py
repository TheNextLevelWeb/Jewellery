from django.db import models
from users.models import Users


class GiftCard(models.Model):
    code = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_redeemed = models.BooleanField(default=False)
    redeemed_by = models.ForeignKey(
        Users, null=True, blank=True, on_delete=models.SET_NULL)
    redeemed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.code
