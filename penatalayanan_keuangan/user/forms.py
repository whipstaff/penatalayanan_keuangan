from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Staff as stf
from main.models import (
    Pospel,
    Sektor,
    Posisi,
    Keluarga,
    Anggota,
    Staff,
    Keuangan,
    KeuanganPospel,
)
from django import forms
from django.contrib.admin.decorators import display
from django.template.loader import get_template


class AddStaffForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Username",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Konfirmasi Password",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Email",
            }
        ),
    )

    class Meta:
        model = stf
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(AddStaffForm, self).save(commit=False)
        # user.email = self.instance.email
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nama Pengguna",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Kata Sandi",
            }
        ),
    )

    class Meta:
        # model = Verifikator
        fields = ("username", "password")


class KeluargaForm(forms.ModelForm):
    keluarga = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Keluarga",
            }
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Keluarga
        fields = ("keluarga",)
