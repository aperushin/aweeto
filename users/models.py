from django.contrib.auth.models import AbstractUser
from django.db import models

from ads.models import Location


class UserRoles(models.TextChoices):
    MEMBER = ('member', 'Member')
    MODERATOR = ('moderator', 'Moderator')
    ADMIN = ('admin', 'Admin')


class User(AbstractUser):
    role = models.CharField(max_length=9, choices=UserRoles.choices, default='member')
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
        db_table = 'ads_user'
