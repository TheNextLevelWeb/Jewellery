from django.db import models

class NearByStores(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=18)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    days = models.CharField(max_length=20)
    openAt = models.CharField(max_length=20)
    closeAt = models.CharField(max_length=20)

    def __str__(self):
        return self.name
