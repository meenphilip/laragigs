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
