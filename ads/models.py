from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    ROLES = (
        ('member', 'Member'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin')
    )

    role = models.CharField(max_length=9, choices=ROLES, default='member')
    age = models.PositiveSmallIntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
