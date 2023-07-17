from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import Ad, User, Category, Location


admin.site.register(User, UserAdmin)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Location)
