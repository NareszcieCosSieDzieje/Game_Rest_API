from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FirearmList, FirearmDetail

app_name = 'firearms'

urlpatterns = [
    path('firearms/', FirearmList.as_view()),
    path('firearms/<int:pk>/', FirearmDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
