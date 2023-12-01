from django.contrib import admin
from .models import (
    Pospel,
    Sektor,
    Posisi,
    Keluarga,
    Anggota,
    Staff,
    Keuangan,
    KeuanganPospel,
    Category,
    TahunAnggaran,
)

# from user.models import User

# Register your models here.
admin.site.register(Pospel)
admin.site.register(Sektor)
admin.site.register(Posisi)
admin.site.register(Keluarga)
admin.site.register(Anggota)
admin.site.register(Staff)
admin.site.register(Keuangan)
admin.site.register(KeuanganPospel)
admin.site.register(Category)
admin.site.register(TahunAnggaran)
# admin.site.register(User)
