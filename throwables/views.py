from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics
from .models import Throwable
from .serializers import ThrowableSerializer
from utils.mixins import BulkCreateModelMixin, LostUpdateModelMixin
from utils.pagination import CustomPagination


class ThrowableList(mixins.ListModelMixin,
                    BulkCreateModelMixin,
                    generics.GenericAPIView):
    queryset = Throwable.objects.all()
    serializer_class = ThrowableSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kwargs['model_class'] = Throwable
        kwargs['model_serializer_class'] = ThrowableSerializer
        return self.create(request, *args, **kwargs)


class ThrowableDetail(LostUpdateModelMixin):

    queryset = Throwable.objects.all()
    serializer_class = ThrowableSerializer

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
