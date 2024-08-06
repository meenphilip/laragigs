from django.contrib import admin
from .models import Listing


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_title", "location"]
    list_filter = ["created", "company_name", "job_title", "location"]
    search_fields = ["company_name", "job_title", "location", "description"]
    ordering = ["-created", "-company_name", "job_title"]
