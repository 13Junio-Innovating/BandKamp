from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "year", "user"]
        
    user=UserSerializer(read_only=True)