# from main.models import Fakultas, Tipe

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from . import views
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.text import slugify


def exportFunction(request):
    # fakultas = Fakultas.objects.all()
    # tipe = Tipe.objects.all()
    # error = ""
    error = ""
    if "reset-pass" in request.POST:
        old = request.POST.get("old")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        user = authenticate(request, username=request.user, password=old)
        if user is None:
            error = "Current Password Enter Mismatch!"
        else:
            try:
                if password == confirm:
                    try:
                        validate_password(password)
                        u = request.user
                        u.set_password(password)
                        u.save()
                        success = "Password has been changed!"
                        return redirect("dashboard")
                    except ValidationError:
                        error = "Password to Weak!"
                        return redirect("dashboard")
                else:
                    error = "New Password and confirm Password mismatch!"
                    return redirect("dashboard")
            except ValueError:
                error = "Password not changed!"

    export_context = {
        "error": error,
        "semua": "semua",
    }

    return export_context
