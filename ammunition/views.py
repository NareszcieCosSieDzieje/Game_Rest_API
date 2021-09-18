from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics
from .models import Ammunition
from .serializers import AmmunitionSerializer
from utils.mixins import BulkCreateModelMixin, LostUpdateModelMixin
from utils.pagination import CustomPagination


class AmmunitionList(mixins.ListModelMixin,
                     BulkCreateModelMixin,
                     generics.GenericAPIView):
    queryset = Ammunition.objects.all()
    serializer_class = AmmunitionSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kwargs['model_class'] = Ammunition
        kwargs['model_serializer_class'] = AmmunitionSerializer
        return self.create(request, *args, **kwargs)


class AmmunitionDetail(LostUpdateModelMixin):

    queryset = Ammunition.objects.all()
    serializer_class = AmmunitionSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)
