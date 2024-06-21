from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False,null=False)
    phone = models.CharField(max_length=18,null=True)
    feedback = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return f"Feedback from {self.name}"
    