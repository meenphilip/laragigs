# forms.py
from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "company_name",
            "job_title",
            "location",
            "email",
            "website_url",
            "tags",
            "logo",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["company_name"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Example: Alphabet Inc. etc",
            }
        )
        self.fields["job_title"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Example: Senior Laravel Developer",
            }
        )
        self.fields["location"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Example: Remote, Boston MA, etc",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Example@gmail.com",
            }
        )
        self.fields["website_url"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Example: https://www.djangoproject.com",
            },
        )
        self.fields["tags"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Example: Laravel, Backend, Postgres, etc",
            }
        )
        self.fields["logo"].widget.attrs.update(
            {"class": "border border-gray-200 rounded p-2 w-full"}
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Include tasks, requirements, salary, etc",
            }
        )
