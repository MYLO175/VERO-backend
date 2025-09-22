from django.db import models

class WaitlistEntry(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)