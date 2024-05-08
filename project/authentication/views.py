from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegisterForm


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect("portal:")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("auth:login")
    return render(request, "register.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect("auth:login")
