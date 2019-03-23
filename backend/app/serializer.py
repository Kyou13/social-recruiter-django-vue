from rest_framework import serializers
from .models import UserInfo, Like
from django.contrib.auth import update_session_auth_hash

class UserInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserInfo
    fields = ('name', 'screen_name', 'description')

class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = ('user', 'twitter_user')
