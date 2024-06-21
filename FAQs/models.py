from django.db import models

class FAQs(models.Model):

    quetion = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQs'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return str(self.quetion)[:25]+"..." if len(str(self.quetion)) > 25 else str(self.quetion)
    
class PrivacyPolicy(models.Model):

    PrivacyPolicy_Title = models.CharField(max_length=255)
    PrivacyPolicy_Detail = models.TextField()

    def __str__(self):
        return str(self.PrivacyPolicy_Title)[:25]+"..." if len(str(self.PrivacyPolicy_Title)) > 25 else str(self.PrivacyPolicy_Title)
    
