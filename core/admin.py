from django.contrib import admin
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ("email","name","country_code","phone_number","created_at")
    search_fields = ("email","name","phone_number")