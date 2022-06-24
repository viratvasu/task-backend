from rest_framework import serializers
from .models import UserProfile, BlogMetadata


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class BlogMetadataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = BlogMetadata
        fields = "__all__"
