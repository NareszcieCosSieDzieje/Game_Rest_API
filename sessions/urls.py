from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SessionList, SessionDetail

app_name = 'sessions'

urlpatterns = [
    path('sessions/', SessionList.as_view()),
    path('sessions/<int:pk>/', SessionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
