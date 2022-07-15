from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, TheUser

admin.site.register(Event)
admin.site.register(TheUser, UserAdmin)
