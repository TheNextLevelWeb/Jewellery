from django.contrib import admin
from .models import FAQs, PrivacyPolicy

admin.site.register(PrivacyPolicy)
admin.site.register(FAQs)
