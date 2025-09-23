from django.db import models

class WaitlistEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200, blank=True)
    country_code = models.CharField(max_length=8, blank=True)   # e.g. +44
    phone_number = models.CharField(max_length=32, blank=True)  # e.g. 7442027268
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)