from django.shortcuts import render
from .models import MusicModel
from .serializers import MusicSerializerClass
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class music_app_view(ListAPIView):
    queryset = MusicModel.objects.order_by('title')
    serializer_class = MusicSerializerClass
    permission_classes = (permissions.AllowAny,)
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('title','singer_name')

class music_detail_view(RetrieveAPIView):
    queryset = MusicModel.objects.all()
    serializer_class = MusicSerializerClass
    lookup_field = 'id'
    permission_classes = (permissions.AllowAny,)

class trending_music_view(ListAPIView):
    queryset = MusicModel.objects.filter(trending=True)
    serializer_class= MusicSerializerClass
    permission_classes = (permissions.AllowAny,)


