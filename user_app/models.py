from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 't_user'
        verbose_name = '餐廳會員'
        verbose_name_plural = verbose_name


