from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from utils.mixins import BulkCreateModelMixin, LostUpdateModelMixin
from utils.pagination import CustomPagination


class UserList(mixins.ListModelMixin,
               BulkCreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kwargs['model_class'] = User
        kwargs['model_serializer_class'] = UserSerializer
        return self.create(request, *args, **kwargs)


class UserDetail(LostUpdateModelMixin):

    queryset = User.objects.all()
    serializer_class = UserSerializer

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
