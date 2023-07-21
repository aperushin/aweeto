from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Location

admin.site.register(User, UserAdmin)
admin.site.register(Location)
