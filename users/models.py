from django.contrib.auth.models import AbstractUser
from django.db import models

from ads.models import Location


class User(AbstractUser):
    ROLES = (
        ('member', 'Member'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=9, choices=ROLES, default='member')
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
        db_table = 'ads_user'
