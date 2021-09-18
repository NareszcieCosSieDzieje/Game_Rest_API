from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_condition import condition
from typing import Callable, Union, OrderedDict
import copy

from .hash_helpers import get_etag, get_object_hash


# POST EXACTLY ONCE
# FIXME TU JUZ MUSZE HASH DAWAC BO SYGNALY NIE DAJA RADY
def is_object_duplicated(instance: OrderedDict, **kwargs):

    if 'model_class' not in kwargs or 'model_serializer_class' not in kwargs:
        raise Exception  # FIXME

    ModelClass = kwargs['model_class']
    ModelSerializerClass = kwargs['model_serializer_class'] # FIXME JUZ NIE POTRZEBNE

    # No instances found - no possible duplicates.
    all_objects = ModelClass.objects.all() # FIXME DEBIG
    if len(all_objects) == 0:
        return False

    # If there are other objects, compare the hashes.
    instance_request_id = get_object_hash(instance)
    duplicate_exists = False
    try:
        duplicate_instance = ModelClass.objects.get(request_id=instance_request_id)
        duplicate_exists = True
    except Exception as e:  # FIXME DoesNotExist
        print(e)

    return duplicate_exists

    # if duplicate_exists:
    #     return True
    #     # raise Exception('Cannot post the same object again!')  # FIXME jak obsluzyc # FIXME RETURN RESPONSE ! I W WRAPPERACH ZROBIC ZWRACANIE?
    # return False


def filter_data(copied_data: list, **kwargs) -> list:
    duplicated_data_indexes = []
    for idx, serialized_object in enumerate(copied_data):
        if is_object_duplicated(serialized_object, **kwargs):
            duplicated_data_indexes.append(idx)
    return duplicated_data_indexes


class BulkCreateModelMixin(CreateModelMixin):


    # FIXME CO Z PUT EXACTLY ONCE JESLI WIELE DANYCH
    def create(self, request, *args, **kwargs):
        many = True if isinstance(request.data, list) else False
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        # CZY DANE SA SLOWNIKIEM CZY STR
        duplicated_data_indexes = []
        # copied_data = copy.deepcopy(serializer.data) # FIXME jesli lista nawet kuzwa juz nie kopiuj tego
        copied_data = serializer.data
        options = {}
        options['model_class'] = kwargs['model_class']
        options['model_serializer_class'] = kwargs['model_serializer_class']
        if isinstance(copied_data, dict):
            copied_data = [copied_data]
        duplicated_data_indexes = filter_data(copied_data, **options)

        if len(duplicated_data_indexes) > 0:
            # FIXME PAGINATION??
            request_data = request.data
            if not isinstance(request_data, list):
                request_data = [request_data]
            resp = {'error': 'Found data that would be duplicated in the database.',
            'unique_data': [item for idx, item in enumerate(request_data) if idx not in duplicated_data_indexes],
            'duplicate_data': [item for idx, item in enumerate(request_data) if idx in duplicated_data_indexes]
            }
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer) # FIXME WRZUC HASH DO INSTANCJI
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# # TODO CACHE implement not decorator
# class LostUpdateModelMixin(RetrieveModelMixin, UpdateModelMixin):
#
#     # @staticmethod
#     # def create_etag(request, *args, **kwargs):
#     #     instance = self.get_object()
#     #     # TODO: CZY HASHOWAC ITP? plus jakis random string??
#     #     # HASHLIB
#     #     return instance.revision_id
#
#     # def last_modified
#
#     def _check_revision_id(self, request):
#         request_etag = request.META.get('HTTP_IF_MATCH')
#         if request_etag is None:
#             return Response({'error': 'IF_MATCH header is required.'}, status=status.HTTP_400_BAD_REQUEST)
#         instance = self.get_object()
#         if instance.revision_id != request_etag:
#             return Response({'error': 'Object has been updated in the meantime.'}, status=status.HTTP_412_PRECONDITION_FAILED)
#         else:
#             return
#
#     @condition(etag_func=my_etag) #create_etag)
#     def retrieve(self, request, *args, **kwargs):
#         super().retrieve(request, *args, **kwargs)
#
#     @condition(etag_func=my_etag)
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self._check_revision_id(request)
#         # TODO: update the revision id of the object
#         # FIXME
#         # instance.revision_id += 1
#         # serializer = self.get_serializer(instance, partial=True)
#         # serializer.is_valid(raise_exception=True)
#         # FIXME
#         self.perform_update(serializer)
#
#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}
#
#         return Response(serializer.data)


# TODO: CZY JA MOGĘ TO ZAIMPLEMENTOWAC JAKO DEKORATORY @post_exactly_once i @lost_update_problem
class LostUpdateModelMixin(RetrieveUpdateDestroyAPIView):

    def _check_revision_id(self, request, **kwargs):
        request_etag = request.META.get('HTTP_IF_MATCH')
        if request_etag is None:
            return Response({'error': 'IF_MATCH header with matching ETag value is required.'}, status=status.HTTP_400_BAD_REQUEST)
        required_etag = get_etag(**kwargs)
        if required_etag != request_etag:
            return Response({'error': 'Object has been updated in the meantime.'}, status=status.HTTP_412_PRECONDITION_FAILED)
        else:
            return None

    @condition(etag_func=get_etag)
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'revision_id'):
            revision_id = instance.revision_id
            kwargs['revision_id'] = str(revision_id)
        if hasattr(instance, 'request_id'):
            request_id = instance.request_id
            kwargs['request_id'] = request_id
        return self.delegator(request, *args, my_func=super().get, **kwargs)
        # return super().get(request, *args, **kwargs)

    # @condition(etag_func=my_etag)
    # def put(self, request, *args, **kwargs):
    #     return super().put(request, *args, **kwargs)
    #
    # @condition(etag_func=my_etag)
    # def patch(self, request, *args, **kwargs):
    #     result = self._check_revision_id(request)
    #     if result:
    #         return result
    #     return super().patch(request, *args, **kwargs)

    # @condition(etag_func=my_etag)
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     revision_check = self._check_revision_id(request)
    #     if revision_check:
    #         return revision_check
    #     # TODO: update the revision id of the object
    #     instance.revision_id += 1
    #     instance.save()
    #     # serializer = self.get_serializer(instance, partial=True)
    #     # serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'revision_id'):
            revision_id = instance.revision_id
            kwargs['revision_id'] = str(revision_id)
        if hasattr(instance, 'request_id'):
            request_id = instance.request_id
            kwargs['request_id'] = request_id
        result = self._check_revision_id(request, **kwargs)
        if result:
            return result
        return self.delegator(request, *args, my_func=super().put, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if hasattr(instance, 'revision_id'):
            revision_id = instance.revision_id
            kwargs['revision_id'] = str(revision_id)
        if hasattr(instance, 'request_id'):
            request_id = instance.request_id
            kwargs['request_id'] = request_id
        result = self._check_revision_id(request, **kwargs)
        if result:
            return result
        return self.delegator(request, *args, my_func=super().patch, **kwargs)

    @condition(etag_func=get_etag)
    def delegator(self, request, *args, my_func: Callable, **kwargs):
        return my_func(request, *args, **kwargs)
