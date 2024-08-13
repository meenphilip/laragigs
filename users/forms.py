from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Login Form
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Enter your email",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Enter your password",
            }
        )


# User Registration Form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already in use.")
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Enter your username",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Enter your email",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Enter your password",
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "class": "border border-gray-200 rounded p-2 w-full",
                "placeholder": "Confirm your password",
            }
        )
