from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MapList, MapDetail

app_name = 'maps'

urlpatterns = [
    path('maps/', MapList.as_view()),
    path('maps/<int:pk>/', MapDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
