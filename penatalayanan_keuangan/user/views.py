from django.shortcuts import render

# Create your views here.
from ast import If
from logging import exception
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    LoginForm,
)

# from main.models import Author, Verifikator, Administrator
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.contrib import messages
from .models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# from .models import Administrator, Staff

# from .tokens import account_activation_token
# Create your views here.


def login(request):
    context = {}
    user = request.user
    success1 = "Null"
    if "success" in request.session:
        success1 = request.session["success"]
        # print(success)
        del request.session["success"]

    print(success1)
    if user.is_authenticated:
        return redirect("index")

    form = LoginForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=user, password=password)
            auth_login(request, user)
            if user is not None:
                return redirect("dashboard")
    else:
        form = LoginForm()
        context = {
            "title": "Login",
            "section": "Login",
            "form": form,
            "success1": success1,
        }
        return render(request, "user-auth/login.html", context)

    context = {"title": "Login", "section": "Login", "form": form, "success1": success1}
    return render(request, "user-auth/login.html", context)


# def update_profile(request):

#     context = {
#         "title": "Login",
#         "section": "Login",
#     }
#     return render(request, "user-auth/update-profile.html", context)


@login_required
def update_profile(request):
    context = {}
    user = request.user

    # try:
    #     if user.role == "ADMIN":
    #         logged = get_object_or_404(Administrator, user=user)
    #     elif user.role == "STAFF":
    #         logged = get_object_or_404(Staff, user=user)
    #     redirect("dashboard")

    # except:
    #      if user.role == "ADMIN":
    #         form = get_object_or_404(Administrator, user=user)
    #      elif user.role == "STAFF":

    # if request.method == "POST":
    #     if form.is_valid():
    #         update_profile = form.save(commit=False)
    #         update_profile.user = user
    #         update_profile.save()
    #         return redirect("profil")

    context = {
        "title": "Update Profile",
        "section": "Update Profile",
        # "form": form,
    }
    return render(request, "user-auth/update-profile.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("user:login")
