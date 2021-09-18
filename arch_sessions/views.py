from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics
from .models import ArchSession
from .serializers import ArchSessionSerializer
from utils.pagination import CustomPagination


class ArchSessionList(mixins.ListModelMixin,
                      generics.GenericAPIView):
    queryset = ArchSession.objects.all()
    serializer_class = ArchSessionSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ArchSessionDetail(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):

    queryset = ArchSession.objects.all()
    serializer_class = ArchSessionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
