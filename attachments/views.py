from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import Attachment
from .serializers import AttachmentSerializer
from utils.mixins import BulkCreateModelMixin, LostUpdateModelMixin
from utils.pagination import CustomPagination


class AttachmentList(mixins.ListModelMixin,
                     BulkCreateModelMixin,
                     generics.GenericAPIView):

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        kwargs['model_class'] = Attachment
        kwargs['model_serializer_class'] = AttachmentSerializer
        return self.create(request, *args, **kwargs)


class AttachmentDetail(LostUpdateModelMixin):

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

