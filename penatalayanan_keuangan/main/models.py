from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.utils.text import slugify
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.
User = get_user_model()


class TahunAnggaran(models.Model):
    year = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "TahunAnggaran"

    def __str__(self):
        return self.year

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.year)
        super(TahunAnggaran, self).save(*args, **kwargs)


class Pospel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "pospel"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Pospel, self).save(*args, **kwargs)


class Sektor(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "sektor"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Sektor, self).save(*args, **kwargs)


class Posisi(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "posisi"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Posisi, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, blank=True)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    posisi = models.ForeignKey(Posisi, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Staff, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("lihat-profil-user", kwargs={"slug": self.slug})


class Keluarga(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    keluarga = models.CharField(max_length=50)
    tgl_pernikahan = models.DateField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Keluarga"

    def __str__(self):
        return self.keluarga

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.keluarga)
        super(Keluarga, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("detail-keluarga", kwargs={"slug": self.slug})


class Anggota(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    fullname = models.CharField(max_length=100, blank=True)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    keluarga = models.ForeignKey(
        Keluarga, on_delete=models.SET_NULL, null=True, blank=True
    )
    tgl_lahir = models.DateField()
    pekerjaan = models.CharField(max_length=100, blank=True)
    alamat = models.CharField(max_length=100, blank=True)
    sektor = models.ForeignKey(Sektor, on_delete=models.SET_NULL, null=True, blank=True)
    domisili = models.CharField(max_length=100, blank=True)
    posisi = models.ForeignKey(Posisi, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Anggota, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("detail-anggota", kwargs={"slug": self.slug})


class Keuangan(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    uraian = models.TextField(max_length=500)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    tanggal = models.DateField()
    jumlah = models.BigIntegerField(blank=True)
    huria = models.BigIntegerField(blank=True)
    pusat = models.BigIntegerField(blank=True)
    pembangunan = models.BigIntegerField(blank=True)
    jenis = models.BooleanField(default=True)
    kategori = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uraian

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uraian)[:50]
        super(Keuangan, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("keuangan", kwargs={"slug": self.slug})


class KeuanganPospel(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    uraian = models.TextField(max_length=500)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    tanggal = models.DateField()
    debit = models.BigIntegerField(blank=True)
    kredit = models.BigIntegerField(blank=True)
    jenis = models.BooleanField(default=True)
    pospel = models.ForeignKey(Pospel, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uraian

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uraian)[:50]
        super(KeuanganPospel, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("keuangan-pospel", kwargs={"slug": self.slug})
