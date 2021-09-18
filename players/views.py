from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer
from utils.mixins import BulkCreateModelMixin, LostUpdateModelMixin
from utils.pagination import CustomPagination


class PlayerList(mixins.ListModelMixin,
                  BulkCreateModelMixin,
                  generics.GenericAPIView):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kwargs['model_class'] = Player
        kwargs['model_serializer_class'] = PlayerSerializer
        return self.create(request, *args, **kwargs)


class PlayerDetail(LostUpdateModelMixin):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

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

