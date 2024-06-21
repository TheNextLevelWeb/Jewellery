from django.db import models

class Support(models.Model):
    
    issue = models.CharField(max_length=255)
    email = models.EmailField()
    details = models.TextField()

    def __str__(self):
        return self.email
    