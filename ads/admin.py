from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Ad, Category, Location
from users.models import User

admin.site.register(User, UserAdmin)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Location)
