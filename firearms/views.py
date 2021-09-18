from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import Firearm
from .serializers import FirearmSerializer
from utils.mixins import BulkCreateModelMixin, LostUpdateModelMixin
from utils.pagination import CustomPagination


class FirearmList(mixins.ListModelMixin,
                  BulkCreateModelMixin,
                  generics.GenericAPIView):

    queryset = Firearm.objects.all()
    serializer_class = FirearmSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kwargs['model_class'] = Firearm
        kwargs['model_serializer_class'] = FirearmSerializer
        return self.create(request, *args, **kwargs)


class FirearmDetail(LostUpdateModelMixin):

    queryset = Firearm.objects.all()
    serializer_class = FirearmSerializer

