from django.urls import path
from .views import music_app_view,music_detail_view,trending_music_view

urlpatterns = [
    path('api/musicmix/',music_app_view.as_view()),
    path('api/musicmix/<str:id>',music_detail_view.as_view()),
    path('api/musicmix/trends/', trending_music_view.as_view()),
]
