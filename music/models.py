import uuid
from .const import MUSIC_CATEGORY,LANGUAGE_CHOICES
from .utils import music_img, audio_file
from django.db import models
from django.utils.timezone import now


# Create your models here.
class MusicModel(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=MUSIC_CATEGORY)
    cover_img = models.ImageField(upload_to=music_img)
    singer_name= models.CharField(max_length=200)
    audio_file = models.FileField(upload_to=audio_file)
    trending = models.BooleanField(default=False)
    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES)


    def __str__(self):
        return f"{self.title} by {self.singer_name}"