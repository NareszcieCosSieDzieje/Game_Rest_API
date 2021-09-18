from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PlayerList, PlayerDetail

app_name = 'players'

urlpatterns = [
    path('players/', PlayerList.as_view()),
    path('players/<int:pk>/', PlayerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
