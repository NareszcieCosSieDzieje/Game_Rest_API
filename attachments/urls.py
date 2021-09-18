from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AttachmentList, AttachmentDetail

app_name = 'attachments'

urlpatterns = [
    path('attachments/', AttachmentList.as_view()),
    path('attachments/<int:pk>/', AttachmentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
