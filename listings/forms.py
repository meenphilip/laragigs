from django import forms
from .models import Listing


# listing form
class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "company_name",
            "job_title",
            "location",
            "email",
            "tags",
            "logo",
            "description",
        ]
