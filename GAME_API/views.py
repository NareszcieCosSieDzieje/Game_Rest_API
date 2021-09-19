from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.schemas import  get_schema_view
import GAME_API


open_api_view = get_schema_view(title='Game API', description='Full API')

# FIXME
def urls_list_view(request, *args, **kwargs):
    # if request.METHOD == 'GET':
    #     x = GAME_REST_API.urlpatterns
    #     print(f"{x = }")
    #     context = {
    #         'url_resources': {'lol': 'test'}
    #     }
    #     # MOZLIWE ZE SAM UZUPELNIE KONTEKTS
    #     return render(request, 'GAME_REST_API/base.html', context)
    # else:
    #     return Response(request, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    context = {'url_resources': {}}
    xx = GAME_API.urls.urlpatterns
    print(f"{xx = }")
    url_resources = context['url_resources']
    for x in xx:
        if hasattr(x, 'namespace') and hasattr(x, 'pattern') and hasattr(x.pattern, '_route'):
            url_resources[x.namespace] = x.pattern._route

        # if hasattr(x, 'url_patters') and hasattr(x, 'namespace'):
        #     print(x.url_patterns)
        #     print(x.namespace)
        # else:
        #     print(f'doesnt wanna work {x}')
        # print(x.pattern)

    # context = {
    #     'url_resources': {'': 'test'}
    # }
    return render(request, 'GAME_API/urls.html', context)
