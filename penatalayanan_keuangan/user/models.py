from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        STAFF = "STAFF", "Staff"
        ADMIN = "ADMIN", "Admin"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)


class Staff(User):
    base_role = User.Role.STAFF

    class Meta:
        proxy = True
