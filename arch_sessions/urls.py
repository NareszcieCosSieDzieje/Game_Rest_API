from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArchSessionList, ArchSessionDetail

app_name = 'arch_sessions'

urlpatterns = [
    path('arch-sessions/', ArchSessionList.as_view()),
    path('arch-sessions/<int:pk>/', ArchSessionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
