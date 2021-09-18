from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AmmunitionList, AmmunitionDetail

app_name = 'ammunition'

urlpatterns = [
    path('ammunition/', AmmunitionList.as_view()),
    path('ammunition/<int:pk>/', AmmunitionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
