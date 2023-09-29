from rest_framework import serializers
from .models import MusicModel
class MusicSerializerClass(serializers.ModelSerializer):
    class Meta:
        model=MusicModel
        fields='__all__'