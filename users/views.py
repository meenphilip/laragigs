from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


# User login view
def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next_url = request.POST.get("next") or request.GET.get("next")
                    messages.success(request, "Login successful!")
                    return redirect(next_url or "listings")
                else:
                    messages.error(request, "Disabled account.")
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = UserLoginForm()
    return render(request, "users/login.html", {"form": form})


# logout user
def user_logout(request):
    logout(request)
    messages.success(request, "Login successful!")
    return redirect("login")
