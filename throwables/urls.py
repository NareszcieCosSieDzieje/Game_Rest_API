from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ThrowableList, ThrowableDetail

app_name = 'throwables'

urlpatterns = [
    path('throwables/', ThrowableList.as_view()),
    path('throwables/<int:pk>/', ThrowableDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
