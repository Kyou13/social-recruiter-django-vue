from django.contrib import admin
from .models import UserInfo, Like

@admin.register(UserInfo)
class UserInfo(admin.ModelAdmin):
  pass

@admin.register(Like)
class Like(admin.ModelAdmin):
  pass
