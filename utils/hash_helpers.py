import hashlib
from typing import Union, Any


# # FIXME TEST
def get_etag(request=None, *args, **kwargs):
    # TODO: ADD INSTANCE?
    # if 'instance' in kwargs:
    # instance = kwargs['instance']
    # instance.request_id + instance.revision_id
    # return that

    revision_id = kwargs.get('revision_id')
    request_id = kwargs.get('request_id')

    if revision_id:
        if request_id:
            return request_id+revision_id
        return revision_id
    else:
        return "no-match" # FIXME


def get_object_hash(instance: Union[Any, dict], ObjectSerializer=None): # : ModelSerializer
    # FIXME EXCLUDE PRIMARY KEY
    instance_as_dict = instance
    if not isinstance(instance, dict):
        if ObjectSerializer is None:
            raise Exception('Mandatory ObjectSerializer when instance is not a dict and a model.')
        serializer = ObjectSerializer(instance)
        instance_as_dict = serializer.data
    for key in ('id', 'request_id', 'revision_id'):
        if key in instance_as_dict:
            instance_as_dict.pop(key)
    instance_as_str = str(instance_as_dict)
    object_hash = hashlib.md5(instance_as_str.encode('utf-8')).hexdigest()
    return object_hash
