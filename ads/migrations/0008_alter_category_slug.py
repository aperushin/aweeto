# Generated by Django 4.2.3 on 2023-07-28 13:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_reload_intial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
