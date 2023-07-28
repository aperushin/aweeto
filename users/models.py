from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import NotOnDomainValidator, IsOlderThanValidator
from users.utils import calculate_age


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=7, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class UserRoles(models.TextChoices):
    MEMBER = ('member', 'Member')
    MODERATOR = ('moderator', 'Moderator')
    ADMIN = ('admin', 'Admin')


class User(AbstractUser):
    role = models.CharField(max_length=9, choices=UserRoles.choices, default='member')
    email = models.EmailField(unique=True, blank=False, validators=[NotOnDomainValidator('rambler.ru')])
    birth_date = models.DateField(null=True, validators=[IsOlderThanValidator(9)])
    location = models.ManyToManyField(Location)

    @property
    def age(self):
        return calculate_age(self.birth_date)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
