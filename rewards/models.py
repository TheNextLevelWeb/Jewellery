from django.db import models
from users.models import Users
from django.core.validators import MinValueValidator


class Rewards(models.Model):
    rStaus = {("PENDING", 'Pending'),
              ("APPROVED", 'Approved'),
              ("COMPLETE", 'Complete'),
              ("EXPIRED", 'Expired'),
              ("CANCELLED", 'Cancelled'),
              ("AVAILABLE", 'Available'),
              ("REDEEMED", 'Redeemed'),
              ("IN_PROGRESS", 'In Progress'),
              ("ON_HOLD", 'On Hold'),
              ("REJECTED", 'Rejected')}
    
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rewardCoin = models.IntegerField(validators=[MinValueValidator(1)])
    rewardsStatus = models.CharField(max_length=50,choices=rStaus)

    class Meta:
        unique_together = ('username', 'title')

    def __str__(self):
        return f"Reward of {self.username}"
    