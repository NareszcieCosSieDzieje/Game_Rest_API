from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SupplyList, SupplyDetail

app_name = 'supplies'

urlpatterns = [
    path('supplies/', SupplyList.as_view()),
    path('supplies/<int:pk>/', SupplyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
