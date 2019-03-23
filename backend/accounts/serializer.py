from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from accounts.models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=False)

  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')

  def create(self, validated_data):
    return User.objects.create_user(request_data=validated_data)
