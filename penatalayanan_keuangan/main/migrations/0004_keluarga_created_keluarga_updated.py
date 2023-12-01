# Generated by Django 4.1.2 on 2023-08-06 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_anggota_user_keluarga_user_keuangan_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="keluarga",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="keluarga",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
