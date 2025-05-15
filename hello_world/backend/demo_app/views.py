from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def hello_world(request):
    return HttpResponse('hello world')


@api_view(['GET'])
def hello_world_drf(request, *args, **kwargs):
    return Response(data={'msg': 'hello world'})