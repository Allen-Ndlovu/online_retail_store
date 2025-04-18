from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','email','password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated):
        return User.objects.create_user(**validated)
