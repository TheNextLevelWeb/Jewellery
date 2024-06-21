from django.db import models
from users.models import Users


def default_empty_list():
    return []

class Notification_history(models.Model):
    username = models.ForeignKey(
        Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.username}'s notifications"
