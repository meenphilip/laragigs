from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create LIsting modles.
class Listing(models.Model):
    company_name = models.CharField(max_length=250, blank=True)
    job_title = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    website_url = models.URLField()
    tags = TaggableManager()  # Use TaggableManager for tags
    logo = models.ImageField(upload_to="company-logos/", blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created", "company_name"]
        indexes = [models.Index(fields=["-created", "company_name"])]

    def __str__(self):
        return f"{self.company_name}"

    # cononical url
    def get_absolute_url(self):
        return reverse("single-listing", args=[self.id])
