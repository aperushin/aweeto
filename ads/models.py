from django.db import models
from django.core.validators import MinLengthValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class AdSelection(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
