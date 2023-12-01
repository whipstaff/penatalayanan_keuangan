from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.home, name="index"),
    path("staffgereja/", views.dashboard, name="staffgereja"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("anggota_jemaat/<str:slug>", views.anggota_jemaat, name="anggota-jemaat"),
    path("daftar_keluarga/", views.daftar_keluarga, name="daftar-keluarga"),
    # path("keuangan_bitung/", views.keuangan_bitung, name="keuangan-bitung"),
    path("keuangan_pospel/", views.keuangan_pospel, name="keuangan-pospel"),
    path("detail-keluarga/<slug>", views.detailkeluarga, name="detail-keluarga"),
    path("detail-anggota/<slug>", views.detailanggota, name="detail-anggota"),
    path("detail-penerimaan/<slug>", views.detailterima, name="detail-terima"),
    path("detail-pengeluaran/<slug>", views.detailkeluar, name="detail-keluar"),
    path("export-entri/", views.export_entri, name="export-entri"),
    path("staff/", views.staff, name="staff"),
    path("penerimaan/<str:slug>", views.penerimaan, name="penerimaan"),
    path("pengeluaran/<str:slug>", views.pengeluaran, name="pengeluaran"),
]
