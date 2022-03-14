from django.http import HttpResponse
from crawling.module import execute, related_keyword_w2v
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'backend', 'crawling'))
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import api_view
import urllib.parse

def get_tag(request):
    pass


@swagger_auto_schema(
    operation_id="키워드 뉴스 조회",
    method="GET",
    operation_description="키워드 맞춤 뉴스 조회",
    responses={200: openapi.Response("OK",)},
    manual_parameters=[
        openapi.Parameter('query', openapi.IN_QUERY, type='string')],
    )
@api_view(['GET'])
def get_news(request):
    query = request.query_params.get('query', None)
    
    query = urllib.parse.quote(query)
    data = execute(query)
    
    return Response(data)